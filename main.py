from operator import itemgetter
from typing import Union
import yaml

import utils.log_handler as logger
log = logger.log
import settings
from utils.auth_utils import Auth
from csv_parser import Parser
import utils.input_utils as input
from api import *


#----------Loading and Validating Input CSVs----------

def handle_load_csv_headers_mapping(path, parser):
    csv_headers_mapping = {}

    csv = input.handle_load_csv_data("Enter file path to the CSV mapping headers to Plextrac data types", csv_file_path=path)

    for index, header in enumerate(csv['headers']):
        key = csv['data'][0][index]
        if key in parser.get_data_mapping_ids():
            csv_headers_mapping[header] = key
            continue
        
        if key == "":
            csv_headers_mapping[header] = "no_mapping"
        else:
            if input.prompt_continue_anyways( f'ERR: Key <{key}> selected for header <{header}> is not an valid key'):
                csv_headers_mapping[header] = "no_mapping"
            else:
                exit()

    parser.csv_headers_mapping = csv_headers_mapping
    log.success(f'Loaded csv headers mapping')


def handle_load_csv_data_verify(path, parser):
    """
    takes a filepath to a csv, and a list of expected headers and returned the csv data if the headers match
    used as basic error checking that we have the correct csv
    """
    csv = input.handle_load_csv_data("Enter file path to CSV data to import", csv_file_path=path)

    if csv.get('headers') != parser.get_csv_headers():
        log.warning(f'CSV headers read from file\n{csv["headers"]}')
        log.warning(f'Expected headers\n{parser.get_csv_headers()}')
        if input.prompt_retry(f'Loaded {csv.get("file_path")} CSV headers don\'t match headers in Headers Mapping CSV.'):
            return handle_load_csv_data_verify("Enter file path to CSV data to import", "", parser.get_csv_headers())

    parser.csv_data = csv['data']
    log.success(f'Loaded csv data')


def handle_add_report_template_name(report_template_name, parser):
    """
    Checks if the given the report_template_name value from the config.yaml file matches the name of an existing
    Report Template in Plextrac. If the template exists in platform, adds this report template UUID to the template
    for reports created with this script. The result being a Report Template is selected in the proper dropdown
    in platform for all reports created.
    """
    report_templates = []

    response = api.report_template.list(auth.base_url, auth.get_auth_headers(), auth.tenant_id)
    if type(response) == list:
        report_templates = list(filter(lambda x: x['data']['template_name'] == report_template_name, response))

    if len(report_templates) > 1:
        if not input.prompt_continue_anyways(f'report_template_name value \'{report_template_name}\' from config matches {len(report_templates)} Report Templates in platform. No Report Template will be added to reports.'):
            exit()
        return

    if len(report_templates) == 1:
        parser.report_template['template'] = report_templates[0]['data']['doc_id']
        return
    
    if not input.prompt_continue_anyways(f'report_template_name value \'{report_template_name}\' from config does not match any Report Templates in platform. No Report Template will be added to reports.'):
        exit()


def handle_add_findings_template_name(findings_template_name, parser):
    """
    Checks if the given the findings_template_name value from the config.yaml file matches the name of an existing
    Finding Layouts in Plextrac. If the layout exists in platform, adds this findings template UUID to the template
    for reports created with this script. The result being a Finding Layout is selected in the proper dropdown
    in platform for all reports created.
    """
    findings_templates = []

    response = api.findings_layout.list(auth.base_url, auth.get_auth_headers())
    if type(response) == list:
        findings_templates = list(filter(lambda x: x['data']['template_name'] == findings_template_name, response))

    if len(findings_templates) > 1:
        if not input.prompt_continue_anyways(f'findings_template_name value \'{findings_template_name}\' from config matches {len(findings_templates)} Finding Layouts in platform. No Findings Layout will be added to reports.'):
            exit()
        return

    if len(findings_templates) == 1:
        parser.report_template['fields_template'] = findings_templates[0]['data']['doc_id']
        return
    
    if not input.prompt_continue_anyways(f'findings_template_name value \'{findings_template_name}\' from config does not match any Finding Layouts in platform. No Finding Layout will be added to reports.'):
        exit()

#----------End Loading and Validating Input CSVs----------
    

if __name__ == '__main__':
    for i in settings.script_info:
        print(i)
    
    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)

    auth = Auth(args)
    auth.handle_authentication()

    parser = Parser()

    # loads and validates csv data
    log.info(f'---Starting data loading---')
    csv_headers_file_path = ""
    if args.get('csv_headers_file_path') != None and args.get('csv_headers_file_path') != "":
        csv_headers_file_path = args.get('csv_headers_file_path')
        log.info(f'Using csv header file path \'{csv_headers_file_path}\' from config...')
    handle_load_csv_headers_mapping(csv_headers_file_path, parser)
    
    csv_data_file_path = ""
    if args.get('csv_data_file_path') != None and args.get('csv_data_file_path') != "":
        csv_data_file_path = args.get('csv_data_file_path')
        log.info(f'Using csv data file path \'{csv_data_file_path}\' from config...')
    handle_load_csv_data_verify(csv_data_file_path, parser)

    report_template_name = ""
    if args.get('report_template_name') != None and args.get('report_template_name') != "":
        report_template_name = args.get('report_template_name')
        log.info(f'Using report template \'{report_template_name}\' from config...')
        handle_add_report_template_name(report_template_name, parser)

    findings_layout_name = ""
    if args.get('findings_layout_name') != None and args.get('findings_layout_name') != "":
        findings_layout_name = args.get('findings_layout_name')
        log.info(f'Using findings layout \'{findings_layout_name}\' from config...')
        handle_add_findings_template_name(findings_layout_name, parser)

    parser.parse_data()
    parser.display_parser_results()

    if input.prompt_continue_anyways(f'IMPORTANT: Data will be imported into Plextrac.\nPlease view the log file generated from parsing to see if there were any errors.\nIf the data was not parsed correctly, please exit the script, fix the data, and re-run.\nThis will import data into {len(parser.clients)} client(s). The more clients you have the harder it will be to undo this import.'):
        parser.import_data(auth)
        log.info(f'Import Complete. Additional logs were added to {log.LOGS_FILE_PATH}')

    if input.prompt_continue_anyways(f'IMPORTANT: Data will be saved to Ptrac(s).\nYou can save each report as a Ptrac. ONLY report and finding information will be saved. NO ASSET will be added to the Ptrac.\nWould you like to create and save a ptrac for {len(parser.reports)} report(s).'):
        parser.save_data_as_ptrac()
        log.info(f'Ptrac(s) creation complete. File(s) can be found in \'exported-ptracs\' folder. Additional logs were added to {log.LOGS_FILE_PATH}')
    
    exit()
