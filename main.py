import yaml

import settings
import utils.log_handler as logger
log = logger.log
from utils.auth_handler import Auth
import utils.input_utils as input


if __name__ == '__main__':
    for i in settings.script_info:
        print(i)

    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)


    """
    Config File

    The `args` variable (created above) stores all the info entered on the config.yaml file. This is a dictionary created from
    the parsed yaml file.
    
    This is passed to the `Auth` object to try and load the instance URL, username, and password for authentication, but you
    can add other fields you need as well.
    """
    log.info(args)
    log.info(args.get('instance_url'))


    """
    Authenticate to Plextrac Instance

    To handle authentication you can create an Auth object that stores different things needed to make calls to API endpoints.
    This info includes the URL of the PT instance you're authenticated to and user credentials used to successfully authenticate.
    After authentication, it creates and stores the authorization headers sent with requests to API endpoints.

    Below is an example of creating an Auth object. Calling the `handle_authentication` method and passing in the args from the
    config file tries to authenticate you to the PT instance in the config with the user credentials in the config. If either of
    these values are not in the config the user is prompted to enter them on the terminal the script was ran from.
    """
    auth = Auth(args)
    auth.handle_authentication()


    """
    Using Authentication

    After creating an Auth object and getting authenticated, you can use the info stored on this object to call PT API endpoints
    as you build out your script. You can use the following data:

    auth.base_url - the url the user was authenticated to (ex. https://example.plextrac.com)
    auth.get_auth_headers() - returns the current Authorization headers (handles reauthenticating if expired)
    auth.tenant_id - the tenant id the user was authenticated to (required by some endpoints)
    """
    log.info(f'Authenticated to {auth.base_url} on tenant {auth.tenant_id}')
    log.info(f'Authentication headers: {auth.get_auth_headers()}')


    """
    Built-in API Endpoints

    You can use the currently built-out API endpoints in the /api folder. This is a wrapper library that contains the specific URLs of all endpoints.
    
    Use the import statement: import api
    
    You can now make an API request by calling api.<folder>.<file>.<endpoint_name>(parameters...) and adding the necessary parameters. The
    `base_url` and `headers` parameter is required for every endpoint that required authentication. This information is stored on the Auth
    object created in the example above.
    """
    import api

    client_id = "<id_of_client>"
    response = api.clients.get_client(auth.base_url, auth.get_auth_headers(), client_id)


    """
    Retrying API Requests

    If one of the built-in API endpoint's request fails it will retry the same request up to the number of times as specified in the setting.py file.
    When retrying it will print the exception and continue. After this number of failed attempts it will raise exceptions instead of printing them.

    By default the number of retries is 5. Change this in the setting.py file
    """
    # EXAMPLE Built-in API call
    # import api

    # client_id = "<id_of_client>"
    # response = api._v1.clients.get_client(auth.base_url, auth.get_auth_headers(), client_id)
    
    # EXAMPLE Console on Failure
    # >>> [EXCEPTION] Request failed - Get Client. Retrying... (1/5)
    #     Exception: ('Connection aborted.', ConnectionResetError(10054, 'An existing connection was forcibly closed by the remote host', None, 10054, None))
    #     Traceback (most recent call last):
    #     etc...


    """
    Logging Wrapper

    Any logging can be done using a custom wrapper for the Python logging module. This wrapper handles color formatting of logs to the console and optional output file.
    
    Use the import statement, then set the reference to the custom logging wrapper:
    import utils.log_handler as logger
    log = logger.log

    You can now write to logs with log.<message-type>("<message>")

    Define the following logging setting in settings.py:
    - console logging level
    - output file logging level
    - whether the script should save logs to a file
    """
    log.warning("You are warned")
    log.info("Here is some info")
    log.success("Congrats!")


    """
    Bulk Iteration Metrics

    You are able to print metrics about an action using the IterationMetrics object in the log_handler.py. This will manage time tracking and gives you a simple function
    that returns a string of the current iterations metrics. If you are doing an action in a loop, i.e. calling the same endpoint, this can be used to show metrics for
    how long the script has been running and how long it should take to complete.

    Use the import statement, then create a new IterationMetrics object. Note the counter starts upon creation, so this line should go right before the loop:
    from utils.log_handler import IterationMetrics

    metrics = IterationMetrics(<num_items_in_list>)

    Now calling the print_iter_metrics() function will calculate the stats of the current interation, increment to the next iteration, and return a string with the
    calculated metrics. This should be called at the end of a loop.
    """
    import time # only imported in this example to use sleep

    from utils.log_handler import IterationMetrics

    items = range(5)
    metrics = IterationMetrics(len(items)) # time starts ticking when the IterationMetrics object is created
    for i in items:
        log.info("Working...")
        time.sleep(3)
        log.success(f'Finished the work.')
        log.info(metrics.print_iter_metrics())


    """
    Built-in User Input Handling

    You can use a wrapper for the Python input() function by utilizing the input_utils.py. This will add a prefix to all user prompts and
    define some validation rules as to the user input.

    Use the import statement: import utils.input_utils as input
    
    You can now use the following wrapper options:
    - user_options
    - user_list
    - continue_anyways
    - retry
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
        log.info(f'{index+1} - {option}')
    val = input.user_list("Select an option", "That wasn't a valid optoin", len(option_list))
    log.info(f'Selected {val}')

    # continue_anyways
    val = input.continue_anyways("You ran into an example problem")
    log.info(f'Selected {val}')

    # retry
    if input.retry("An example previous input was invalid. Selecting 'n' will exit the script"):
        log.info("You chose to retry instead of exiting the script")


    """
    Built-in General Utility Helper

    There are a handful of helpful functions in the general_utils.py file. These mostly involve data sanitation or validation
    """
