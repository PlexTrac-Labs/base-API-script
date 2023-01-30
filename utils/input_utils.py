import os
import json
import csv

prompt_prefix = "\n[Prompt] "
prompt_suffix = ": "

# prompts user for data not needing validation
def prompt_user(msg):
    return input(prompt_prefix + msg + prompt_suffix)


def user_options(msg, retry_msg="", options=[]):
    """
    Prompts a user for an input from a given list of options, and returns the valid choice.
    
    Parameters:
    msg (str): Message to display with the prompt
    retry_msg (str): Message to display if user enters invalid input, defaults to empty string
    options (list): List of valid options
    
    Returns:
    str: The valid option chosen by the user
    """
    #setup
    str_options = ""
    for i in options:
        str_options += i + "/"
    str_options = str_options[0:-1]
    
    #get input
    entered = input(prompt_prefix + msg + " (" + str_options + ")" + prompt_suffix)
    
    #validate input
    if entered in options:
        return entered

    #ask again
    if retry(retry_msg):
        return user_options(msg, retry_msg, options)


def user_list(msg, retry_msg="", range=0):
    """
    Prompts a user for an input from a given range, and returns the valid choice. Use after printing
    a list of options. This list should display incrementing numbers with each item, from 1 to number
    of options.

    ex.
    1 - first option
    2 - second option
    etc.

    The number return is the 1-based index. If looping through a list you will need to subtract one
    to reference the correct choice.
    
    Parameters:
    msg (str): Message to display with the prompt
    retry_msg (str): Message to display if user enters invalid input, defaults to empty string
    range (int): Number of valid options
    
    Returns:
    int: The valid option chosen by the user
    """
    #setup
    str_options = "1-" + str(range)
    
    #get input
    entered = input(prompt_prefix + msg + " (" + str_options + ")" + prompt_suffix)
    
    #validate input
    if int(entered) > 0 and int(entered) <= range:
        return int(entered)

    #ask again
    if retry(retry_msg):
        return user_list(msg, retry_msg, range)


def continue_anyways(msg):
    """
    Prompts a user whether they want to continue despite a potentially problematic input.
    
    Parameters:
    msg (str): Message to display with the prompt
    
    Returns:
    bool: True if user wants to continue, False if user does not want to continue
    """
    entered = input(prompt_prefix + msg + " Continue Anyways? (y/n)" + prompt_suffix)
    if entered == 'y':
        return True
    elif entered == 'n':
        return False
    else:
        return continue_anyways(msg)

        
def retry(msg):
    """
    Prompts a user if they want to retry the last input option. This will either return a True boolean
    or exit the script.
    
    Parameters:
    msg (str): Message to display with the prompt
    
    Returns:
    bool: True if user wants to retry
    """
    entered = input(prompt_prefix + msg + " Try Again? (y/n)" + prompt_suffix)
    if entered == 'y':
        return True
    else:
        exit()




# gets the file path of a json to be imported, checks if the file exists, and trys to load and return the data
def load_json_data(msg, json_file_path=""):
    if json_file_path == "":
        json_file_path = prompt_user(msg + "(relative file path, including file extention)")

    if not os.path.exists(json_file_path):
        if retry(f'Specified JSON file at \'{json_file_path}\' does not exist.'):
            return load_json_data(msg)
    
    try:
        with open(json_file_path, 'r', encoding="utf8") as file:
            json_data = {
                "file_path": json_file_path,
                "data": json.load(file)
            }
    except Exception as e:
        if retry(f'Error loading file: {e}'):
            return load_json_data(msg)
    
    return json_data


# gets the file path of a csv to be imported, checks if the file exists, and trys to load and return the data
def load_csv_data(msg, csv_file_path=""):
    if csv_file_path == "":
        csv_file_path = prompt_user(msg + " (relative file path, including file extention)")

    if not os.path.exists(csv_file_path):
        if retry(f'Specified CSV file at \'{csv_file_path}\' does not exist.'):
            return load_csv_data(msg)

    try:
        with open(csv_file_path, 'r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)

            csv_complete = []

            for row in reader:
                csv_complete.append(row)

            csv_headers = csv_complete[0]
            csv_data = csv_complete[1:]

            return {
                "file_path": csv_file_path,
                "csv": csv_complete,
                "headers": csv_headers,
                "data": csv_data
            }

    except Exception as e:
        if retry(f'Error loading file: {e}'):
            return load_csv_data(msg)
