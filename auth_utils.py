from getpass import getpass

from input_utils import *
from request_utils import *

class Auth():
    
    def __init__(self, base_url):
        self.base_url = base_url
        self.tenant_id = None
        self.username = None
        self.password = None
    
        self.auth_headers = {}

    def add_auth_header(self, authorization_token):
        self.auth_headers["Authorization"] = authorization_token

    def add_cf_auth_header(self, cf_token):
        self.auth_headers["cf-access-token"] = cf_token


    def handle_auth(self):
        print('\n---Starting Authorization---')

        if self.username == None:
            self.username = prompt_user("Please enter your PlexTrac username: ")
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
                return self.handle_auth()
        
        self.tenant_id = response.get('tenant_id')

        if response.get('mfa_enabled'):
            print('MFA detected for user')

            mfa_auth_data = {
                "code": response.get('code'),
                "token": prompt_user("Please enter your 6 digit MFA code: ")
            }
            
            response = request_mfa_authenticate(self.base_url, self.auth_headers, mfa_auth_data)
            if response.get('status') != "success":
                if prompt_retry("Invalid MFA Code."):
                    return self.handle_auth()

        self.add_auth_header(response['token'])
        print('Success! Authenticated')
        return self.auth_headers


