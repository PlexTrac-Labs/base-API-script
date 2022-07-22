import requests
import json

from request_utils import *


prompt_prefix = "\n[Prompt] "

# prompts user for data not needing validation
def prompt_user(msg):
    return input(prompt_prefix + msg)


# prompts users for an input. checks the entered input against valid options. returns a valid choice
def prompt_user_options(msg, retry_msg="", options=[]):
    #setup
    str_options = ""
    for i in options:
        str_options += i + "/"
    str_options = str_options[0:-1]
    
    #get input
    entered = input(prompt_prefix + msg + " (" + str_options + "): ")
    
    #validate input
    if entered in options:
        return entered

    #ask again
    if prompt_retry(retry_msg):
        return prompt_user_options(msg, retry_msg, options)


# prompts user if they want to ignore the last, potentially problematic, input option
def prompt_continue_anyways(msg):
    entered = input(prompt_prefix + msg + " Continue Anyways? (y/n): ")
    if entered == 'y':
        return True
    elif entered == 'n':
        return False
    else:
        return prompt_continue_anyways(msg)

        
# prompts the users if they want to retry the last input option
def prompt_retry(msg):
    entered = input(prompt_prefix + msg + " Try Again? (y/n): ")
    if entered == 'y':
        return True
    elif entered == 'n':
        exit()
    else:
        return prompt_retry(msg)








# prompts user for their plextrac url, checks that the API is up and running, then returns the url
def handle_instance_url():
    base_url = prompt_user("Please enter the full URL of your PlexTrac instance (with protocol): ")

    #validate
    try:
        response = requests.get(f'{base_url}/api/v1/') # could be refractored to use request utils

        try:
            response_json = json.loads(response.text)

            if response_json['text'] == "Authenticate at /authenticate":
                print("Validated instance URL")
                return {
                    "base_url": base_url,
                    "cf_token": None
                }
        except Exception as e: # potential plextrac internal instance running behind Cloudflare
            option = prompt_user_options("That URL points to a running verson of Plextrac. However, the API did not respond.\nThere might be an additional layer of security. Try adding Cloudflare auth token?", "Do you want to try adding a Cloudflare token?", ['y', 'n'])    
            if option == 'y':
                return handle_cf_instance_url(base_url)
            
            if prompt_retry("Could not validate instance URL."):
                return handle_instance_url()


    except Exception as e:
        # print("Exception: ", e)
        if prompt_retry("Could not validate URL. Either the API is offline or it was entered incorrectly\nExample: https://company.plextrac.com"):
            return handle_instance_url()


# handles extra layer of Cloudflare authorization
# plextrac test instances are hosted behind a Cloudflare wall that requires another layer of authorization
def handle_cf_instance_url(base_url):
    cf_token = prompt_user("Please enter your active 'CF_Authorization' token: ")
    response = requests.get(f'{base_url}/api/v1/', headers={"cf-access-token": cf_token}) # could be refractored to use request utils
            
    try:
        response_json = json.loads(response.text)

        if response_json['text'] == "Authenticate at /authenticate":
            print("Success! Validated instance URL")
            return {
                "base_url": base_url,
                "cf_token": cf_token
            }
    except Exception as e:
        if prompt_retry("Could not validate instance URL."):
            return handle_instance_url()
