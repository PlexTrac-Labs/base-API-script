from getpass import getpass
from operator import itemgetter

from input_utils import *
from request_utils import *

class Auth():
    
    def __init__(self, args):
        self.base_url = args.get('instance_url')
        self.cf_token = args.get('cf_token')
        self.username = args.get('username')
        self.password = args.get('password')
        self.tenant_id = None
        self.auth_headers = {}


    def add_auth_header(self, authorization_token):
        self.auth_headers["Authorization"] = authorization_token


    def add_cf_auth_header(self, cf_token):
        self.auth_headers["cf-access-token"] = cf_token

    # checks is authorization is current and returns headers, otherwise tries to re-authenticate and return new auth headers
    def get_auth_headers(self):
        try:
            response = requests.get(f'{self.base_url}/api/v2/whoami', headers=self.auth_headers)

            if response.status_code == 200:
                try:
                    response_json = json.loads(response.text)
                    if response_json.get('authentication_provider') != None:
                        return self.auth_headers
                except Exception as e:
                    print("Cloudflare Authorization Expired")
                    self.handle_authentication()
                    return self.auth_headers
            else:
                print("Authorization Expired")
                self.handle_authentication()
                return self.auth_headers
        except Exception as e:
            print("Could not validate authentication headers. Is the API offline?")
            self.handle_authentication()
            return self.auth_headers


    # prompts user for their plextrac url, checks that the API is up and running, then sets the url
    def handle_instance_url(self):
        if self.base_url == None:
            self.base_url = prompt_user("Please enter the full URL of your PlexTrac instance (with protocol)")

        #validate
        try:
            response = requests.get(f'{self.base_url}/api/v1/') # could be refractored to use request utils

            try:
                response_json = json.loads(response.text)

                if response_json['text'] == "Authenticate at /authenticate":
                    print("Success! Validated instance URL")
                    
            except Exception as e: # potential plextrac internal instance running behind Cloudflare
                if self.cf_token == None:
                    option = prompt_user_options("That URL points to a running verson of Plextrac. However, the API did not respond.\nThere might be an additional layer of security. Try adding Cloudflare auth token?", "Do you want to try adding a Cloudflare token?", ['y', 'n'])    
                    if option == 'y':
                        return self.handle_cf_instance_url()
                else:
                    return self.handle_cf_instance_url()
            
                if prompt_retry("Could not validate instance URL."):
                    self.cf_token = None
                    return self.handle_instance_url()

        except Exception as e:
            # print("Exception: ", e)
            if prompt_retry("Could not validate URL. Either the API is offline or it was entered incorrectly\nExample: https://company.plextrac.com"):
                self.base_url = None
                return self.handle_instance_url()


    # handles extra layer of Cloudflare authorization
    # plextrac test instances are hosted behind a Cloudflare wall that requires another layer of authorization
    def handle_cf_instance_url(self):
        if self.cf_token == None:
            self.cf_token = prompt_user("Please enter your active 'CF_Authorization' token")

        response = requests.get(f'{self.base_url}/api/v1/', headers={"cf-access-token": self.cf_token}) # could be refractored to use request utils
            
        try:
            response_json = json.loads(response.text)

            if response_json['text'] == "Authenticate at /authenticate":
                self.add_cf_auth_header(self.cf_token)
                print("Success! Validated instance URL")
                
        except Exception as e:
            if prompt_retry("Could not validate instance URL."):
                self.cf_token = None
                return self.handle_instance_url()


    def handle_authentication(self):
        print('\n---Starting Authorization---')

        self.handle_instance_url()

        if self.username == None:
            self.username = prompt_user("Please enter your PlexTrac username")
        if self.password == None:
            self.password = getpass(prompt="Password: ")
        
        authenticate_data = {
            "username": self.username,
            "password": self.password
        }
        
        response = request_authenticate(self.base_url, self.auth_headers, authenticate_data)
        
        # the following conditional can fail due to:
        # - invalid credentials
        # - if the instance is setup to requre mfa and use user does not have mfa setup
        # - other
        # the api response is purposely non-descript to prevent gaining information about the authentication process
        if response.get('status') != "success":
            if prompt_retry("Could not authenticate with entered credentials."):
                self.username = None
                self.password = None
                self.tenant_id = None
                return self.handle_authentication()
        
        self.tenant_id = response.get('tenant_id')

        if response.get('mfa_enabled'):
            print('MFA detected for user')

            mfa_auth_data = {
                "code": response.get('code'),
                "token": prompt_user("Please enter your 6 digit MFA code")
            }
            
            response = request_mfa_authenticate(self.base_url, self.auth_headers, mfa_auth_data)
            if response.get('status') != "success":
                if prompt_retry("Invalid MFA Code."):
                    return self.handle_authentication()

        self.add_auth_header(response['token'])
        print('Success! Authenticated')
