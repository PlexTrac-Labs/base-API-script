import os
import json
import csv
from typing import List

prompt_prefix = "\n[Prompt] "
prompt_suffix = ": "

# prompts user for data not needing validation
def prompt_user(msg):
    return input(prompt_prefix + msg + prompt_suffix)


def user_options(msg: str, retry_msg: str ="", options: List[str] = []) -> str:
    """
    Prompts a user for an input from a given list of options, and returns the valid choice.

    :param msg: message to display with the prompt
    :type msg: str
    :param retry_msg: message to display if user enters invalid input, defaults to ""
    :type retry_msg: str, optional
    :param options: list of valid options, defaults to []
    :type options: List[str], optional
    :return: the valid option chosen by the user
    :rtype: str
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


def user_list(msg: str, retry_msg: str = "", range: int = 0) -> int:
    """
    Prompts a user for an input from a given range, and returns the valid choice. Call this method after printing
    a list of options. This list should display incrementing numbers with each item, from 1 to number
    of options.

    ex.
    1 - first option
    2 - second option
    etc.

    The number return is the 1-based index. If looping through a list you will need to subtract one
    to reference the correct choice.

    :param msg: message to display with the prompt
    :type msg: str
    :param retry_msg: message to display if user enters invalid input, defaults to ""
    :type retry_msg: str, optional
    :param range: number of valid options, defaults to 0
    :type range: int, optional
    :return: the valid option chosen by the user
    :rtype: int
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


def continue_check(msg: str) -> bool:
    """
    Prompts a user whether they want to continue, by adding the string " Continue? (y/n)"
    to the end of the `msg` passed in. This is similar to continue_anyways, but doesn't
    mean something bad might happen. This can be used for general checkpoints in a script.

    :param msg: message to display with the prompt
    :type msg: str
    :return: True if user types "y" else False
    :rtype: bool
    """    
    entered = input(prompt_prefix + msg + " Continue? (y/n)" + prompt_suffix)
    if entered == 'y':
        return True
    else:
        return False


def continue_anyways(msg: str) -> bool:
    """
    Prompts a user whether they want to continue despite a potentially problematic input,
    by adding the string " Continue Anyways? (y/n)" to the end of the `msg` passed in.

    :param msg: message to display with the prompt
    :type msg: str
    :return: True if user types "y" else False
    :rtype: bool
    """    
    entered = input(prompt_prefix + msg + " Continue Anyways? (y/n)" + prompt_suffix)
    if entered == 'y':
        return True
    else:
        return False

        
def retry(msg: str) -> bool:
    """
    Prompts a user if they want to retry the last input option. This will either return a True boolean
    or exit the script.

    :param msg: message to display with the prompt
    :type msg: str
    :return: True if user wants to retry otherwise the the script will exit
    :rtype: bool
    """    
    entered = input(prompt_prefix + msg + " Try Again? (y/n)" + prompt_suffix)
    if entered == 'y':
        return True
    else:
        exit()


class LoadedJSONData():
    def __init__(self, file_path: str, data: dict):
        self.file_path = file_path
        self.data = data

def load_json_data(msg: str, json_file_path: str = "") -> LoadedJSONData:
    """
    Returns a LoadedJSONData with the loaded JSON data. If unsuccessful loading file, continues prompting user until successful or exits the script.

    LoadedJSONData : {
        "file_path": csv_file_path,
        "data": data loaded from JSON file
    }

    :param msg: custom message to tell the user which file they should enter the file path of
    :type msg: str
    :param json_file_path: file path to JSON file to load, defaults to ""
    :type json_file_path: str, optional
    :return: object with loaded JSON data and the file path the data was loaded from
    :rtype: LoadedJSONData
    """    
    if json_file_path == "":
        json_file_path = prompt_user(msg + "(relative file path, including file extention)")

    if not os.path.exists(json_file_path):
        if retry(f'Specified JSON file at \'{json_file_path}\' does not exist.'):
            return load_json_data(msg)
    
    try:
        with open(json_file_path, 'r', encoding="utf8") as file:
            json_data = json.load(file)
    except Exception as e:
        if retry(f'Error loading file: {e}'):
            return load_json_data(msg)
    
    return LoadedJSONData(file_path=json_file_path, data=json_data)


class LoadedCSVData():
    def __init__(self, file_path: str, csv: List[List[str]], headers: List[str], data: List[str] | List[List[str]]):
        self.file_path = file_path
        self.csv = csv
        self.headers = headers
        self.data = data

def load_csv_data(msg: str, csv_file_path: str = "") -> LoadedCSVData:
    """
    Returns a LoadedCSVData with the loaded CSV data. If unsuccessful loading file, continues prompting user until successful or exits the script.

    LoadedCSVData : {
        "file_path": csv_file_path,
        "csv": List[row List[val]] list of rows, each row being a list of column values. Including header row
        "headers": List[val] of csv header values
        "data": List[row List[val]] list of rows, each row being a list of column values. Excluding header row
    }

    :param msg: custom message to tell the user which file they should enter the file path of
    :type msg: str
    :param csv_file_path: file path to CSV file to load, defaults to ""
    :type csv_file_path: str, optional
    :return: object with loaded CSV data and the file path the data was loaded from
    :rtype: LoadedCSVData
    """    
    if csv_file_path == "":
        csv_file_path = prompt_user(msg + " (relative file path, including file extention)")

    if not os.path.exists(csv_file_path):
        if retry(f'Specified CSV file at \'{csv_file_path}\' does not exist.'):
            return load_csv_data(msg)

    try:
        # if running into errors with reading a loaded csv, check the encoding
        #
        # changed default encoding from 'utf-8' to 'utf-8-sig'. This generally
        # works better when the input is either a CSV vs a UTF-8 CSV. Should
        # remove the BOM char '\ufeff' from the beginning of the first cell value
        with open(csv_file_path, 'r', newline='', encoding='utf-8-sig') as f:
            reader = csv.reader(f)

            csv_complete = []

            for row in reader:
                csv_complete.append(row)

            csv_headers = csv_complete[0]

            # depending on encoding, empty cells at the end of a row might be counted as empty strings "" or not added
            # (i.e. each row of the CSV might be a different length array)
            # the following processing makes sure each row of the CSV is the same length
            for row in csv_complete[1:]:
                if len(row) < len(csv_headers):
                    for i in range(len(csv_headers) - len(row)):
                        row.append("")
                        
            csv_data = csv_complete[1:]

            return LoadedCSVData(file_path=csv_file_path, csv=csv_complete, headers=csv_headers, data=csv_data)

    except Exception as e:
        if retry(f'Error loading file: {e}'):
            return load_csv_data(msg)
