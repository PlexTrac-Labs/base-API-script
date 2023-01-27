import yaml

import settings
import utils.log_handler as logger
log = logger.log
from utils.auth_utils import Auth
import utils.input_utils as input


if __name__ == '__main__':
    for i in settings.script_info:
        print(i)

    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)


    """
    Authenticate to Plextrac Instance

    Creates auth object to handle authentication, initializes with values in config
    Tries to authenticate, will use values stored or prompt the user if needed
    """
    auth = Auth(args)
    auth.handle_authentication()


    """
    Using Authentication

    Starting from this authentication example, you can now build out your script and call other endpoints
    The call to auth.handle_authenticate() above will authenticate the user and update the auth obj to hold all authentication information
    When calling an endpoint you can use the following data

    auth.base_url - the url the user was authenticated to (ex. https://example.plextrac.com)
    auth.get_auth_headers() - to get current Authorization headers (handles reauthenticating if expired)
    auth.tenant_id - to get the tenant id the user was authenticated to (required by some endpoints)
    """
    log.info(f'Aauthenticated to {auth.base_url} on tenant {auth.tenant_id}')
    log.info(f'Authentication headers: {auth.get_auth_headers()}')


    """
    Built-in API Endpoints

    You can use the currently built-out API endpoints in the /api folder. This is a wrapper that contains the specific url of certain endpoints.
    
    Use the import statement: from api import *
    
    You can now make a request by calling api.<object>.<endpoint>() and adding the necessary parameters
    ex: response = api.client.get(auth.base_url, auth.get_auth_headers(), client_id)
    """


    """
    Logging Wrapper

    Any logging can be done using a custom wrapper for the Python logging module. This wrapper handles color formatting of logs to the console and optional output file.
    
    Use the import statement, then set the reference to the custom logging wrapper:
    import utils.log_handler as logger
    log = logger.log

    You can now write to logs with log.<message-type>(<message>)

    Define the following logging setting in settings.py:
    - console logging level
    - output file logging level
    - whether the script should save logs to a file
    """
    log.warning("You are warned")
    log.info("Here is some info")
    log.success("Congrats!")


    """
    Built-in User Input Handling

    You can use a wrapper for the Python input() function by utilizing the input_utils.py. This will add a prefix to all user prompts and
    define some validation rules as to the user input.

    Use the import statement: import utils.input_utils as input
    
    You can now use the following wrapper options:
    - user_options
    - user_list
    - retry
    - continue_anyways
    - load_json_data
    - load_csv_data

    All options will continue to prompt the user until a valid input has been entered or selected, or exit the script.
    """
    # user_options
    val = input.user_options("Select an option", "That wasn't a valid optoin", ["1", "2", "3"])
    log.info(f'Selected {val}')

    # user_list
    option_list = ["apple", "banana", "pear"]
    for index, option in enumerate(option_list):
        log.info(f'{index} - {option}')
    val = input.user_list("Select an option", "That wasn't a valid optoin", len(option_list))
    log.info(f'Selected {val}')

    # continue_anyways
    val = input.continue_anyways("You ran into an example problem")
    log.info(f'Selected {val}')
