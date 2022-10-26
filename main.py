from operator import itemgetter
from typing import Union
import yaml

from input_utils import *
from auth_utils import *
from request_utils import *
from csv_parser import *


script_info = ["====================================================================",
               "= General CSV Import Script                                        =",
               "=------------------------------------------------------------------=",
               "= Takes a CSV with rows representing client, report, finding and   =",
               "= asset data and a CSV with how to map each column to a            =",
               "= location in Plextrac. Parses the CSV and import data to Plextrac =",
               "===================================================================="
            ]


#----------Loading and Validating Input CSVs----------

def handle_load_csv_headers_mapping(path, parser):
    csv_headers_mapping = {}

    csv = handle_load_csv_data("Enter file path to the CSV mapping headers to Plextrac data types", csv_file_path=path)

    for index, header in enumerate(csv['headers']):
        key = csv['data'][0][index]
        if key in parser.get_data_mapping_ids():
            csv_headers_mapping[header] = key
            continue
        
        if key == "":
            csv_headers_mapping[header] = "no_mapping"
        else:
            if prompt_continue_anyways( f'ERR: Key <{key}> selected for header <{header}> is not an valid key'):
                csv_headers_mapping[header] = "no_mapping"
            else:
                exit()

    parser.csv_headers_mapping = csv_headers_mapping
    print(f'Success! Loaded csv headers mapping')


def handle_load_csv_data_verify(path, parser):
    """
    takes a filepath to a csv, and a list of expected headers and returned the csv data if the headers match
    used as basic error checking that we have the correct csv
    """
    csv = handle_load_csv_data("Enter file path to CSV data to import", csv_file_path=path)

    if csv.get('headers') != parser.get_csv_headers():
        print(f'Debug: CSV headers read from file\n{csv["headers"]}')
        print(f'Debug: Expected headers\n{parser.get_csv_headers()}')
        if prompt_retry(f'Loaded {csv.get("file_path")} CSV headers don\'t match headers in Headers Mapping CSV.'):
            return handle_load_csv_data_verify("Enter file path to CSV data to import", "", parser.get_csv_headers())

    parser.csv_data = csv['data']
    print(f'Success! Loaded csv data')

#----------End Loading and Validating Input CSVs----------
    

if __name__ == '__main__':
    for i in script_info:
        print(i)
    
    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)

    auth = Auth(args)
    auth.handle_authentication()

    parser = Parser()

    # loads and validates csv data
    print(f'\n---Starting data loading---')
    csv_headers_file_path = ""
    if args.get('csv_headers_file_path') != None and args.get('csv_headers_file_path') != "":
        csv_headers_file_path = args.get('csv_headers_file_path')
        print(f'Using csv header file path \'{csv_headers_file_path}\' from config...')
    handle_load_csv_headers_mapping(csv_headers_file_path, parser)
    
    csv_data_file_path = ""
    if args.get('csv_data_file_path') != None and args.get('csv_data_file_path') != "":
        csv_data_file_path = args.get('csv_data_file_path')
        print(f'Using csv data file path \'{csv_data_file_path}\' from config...')
    handle_load_csv_data_verify(csv_data_file_path, parser)

    parser.parse_data()
    parser.display_parser_results()

    print(f'IMPORTANT: Data will be imported into Plextrac.')
    print(f'Please view the log file generated from parsing to see if there were any errors.')
    print(f'If the data was not parsed correctly, please exit the script, fix the data, and re-run.')

    if prompt_continue_anyways(f'\nThis will import data into {len(parser.clients)} client(s). The more clients you have the harder it will be to undo this import.'):
        parser.import_data(auth)
        print(f'Import Complete\nAdditional logs were added to {parser.LOGS_FILE_PATH}')
    
    exit()
