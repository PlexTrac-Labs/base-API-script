import time
import csv
from uuid import uuid4
from copy import copy, deepcopy
import logging
import re

import general_utils as utils
from input_utils import *

class Parser():
    
    # list of locations to store data in Plextrac and how to access that location
    data_mapping = {
        'no_mapping': {
            'id': 'no_mapping',
            'object_type': 'IGNORE',
            'data_type' : 'IGNORE',
            'validation_type': None,
            'input_blanks': False,
            'path': []
        },
        # CLIENT INFO
        'client_name': {
            'id': 'client_name',
            'object_type': 'CLIENT',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['name']
        },
        'client_poc': {
            'id': 'client_poc',
            'object_type': 'CLIENT',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['poc']
        },
        'client_poc_email': {
            'id': 'client_poc_email',
            'object_type': 'CLIENT',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['poc_email']
        },
        'client_description': {
            'id': 'client_description',
            'object_type': 'CLIENT',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['description']
        },
        'client_tag': {
            'id': 'client_tag',
            'object_type': 'CLIENT',
            'data_type' : 'TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'client_multi_tag': {
            'id': 'client_multi_tag',
            'object_type': 'CLIENT',
            'data_type' : 'MULTI_TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'client_custom_field': {
            'id': 'client_custom_field',
            'object_type': 'CLIENT',
            'data_type' : 'CUSTOM_FIELD',
            'validation_type': None,
            'input_blanks': True,
            'path': ['custom_field', 'INDEX']
        },
        # REPORT INFO
        'report_name': {
            'id': 'report_name',
            'object_type': 'REPORT',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['name']
        },
        'report_start_date': {
            'id': 'report_start_date',
            'object_type': 'REPORT',
            'data_type' : 'DETAIL',
            'validation_type': "DATE_ZULU",
            'input_blanks': False,
            'path': ['start_date'] # validate
        },
        'report_end_date': {
            'id': 'report_end_date',
            'object_type': 'REPORT',
            'data_type' : 'DETAIL',
            'validation_type': "DATE_ZULU",
            'input_blanks': False,
            'path': ['end_date'] # validate
        },
        'report_tag': {
            'id': 'report_tag',
            'object_type': 'REPORT',
            'data_type' : 'TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'report_multi_tag': {
            'id': 'report_multi_tag',
            'object_type': 'REPORT',
            'data_type' : 'MULTI_TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'report_custom_field': {
            'id': 'report_custom_field',
            'object_type': 'REPORT',
            'data_type' : 'CUSTOM_FIELD',
            'validation_type': None,
            'input_blanks': True,
            'path': ['custom_field', 'INDEX']
        },
        'report_narrative': {
            'id': 'report_narrative',
            'object_type': 'REPORT',
            'data_type' : 'NARRATIVE',
            'validation_type': None,
            'input_blanks': True,
            'path': ['exec_summary', 'custom_fields', 'INDEX']
        },
        # FINDING INFO
        'finding_assigned_to': {
            'id': 'finding_assigned_to',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['assignedTo'] # document email
        },
        'finding_created_at': {
            'id': 'finding_created_at',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': "DATE_EPOCH",
            'input_blanks': False,
            'path': ['createdAt'] # validate
        },
        'finding_closed_at': {
            'id': 'finding_closed_at',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': "DATE_EPOCH",
            'input_blanks': False,
            'path': ['closedAt'] # validate
        },
        'finding_description': {
            'id': 'finding_description',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['description']
        },
        'finding_recommendations': {
            'id': 'finding_recommendations',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['recommendations']
        },
        'finding_references': {
            'id': 'finding_references',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['references']
        },
        'finding_severity': {
            'id': 'finding_severity',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': "SEVERITY",
            'input_blanks': False,
            'path': ['severity'] # validate
        },
        'finding_status': {
            'id': 'finding_status',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': "STATUS",
            'input_blanks': False,
            'path': ['status'] # validate
        },
        'finding_sub_status': {
            'id': 'finding_sub_status',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['subStatus']
        },
        'finding_multi_tag': {
            'id': 'finding_multi_tag',
            'object_type': 'FINDING',
            'data_type' : 'MULTI_TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'finding_title': {
            'id': 'finding_title',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['title']
        },
        'finding_custom_field': {
            'id': 'finding_custom_field',
            'object_type': 'FINDING',
            'data_type' : 'KEY_CUSTOM_FIELD',
            'validation_type': None,
            'input_blanks': True,
            'path': ['fields']
        },
        'finding_cvss3_1_overall': {
            'id': 'finding_cvss3_1_overall',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': 'FLOAT', # validate
            'input_blanks': False,
            'path': ['risk_score', 'CVSS3_1', 'overall']
        },
        'finding_cvss3_1_vector': {
            'id': 'finding_cvss3_1_vector',
            'object_type': 'FINDING',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['risk_score', 'CVSS3_1', 'vector']
        },
        'finding_cve': {
            'id': 'finding_cve_name',
            'object_type': 'FINDING',
            'data_type' : 'CVE',
            'validation_type': None,
            'input_blanks': False,
            'path': ['common_identifiers', 'CVE', 'INDEX'] # document CVE-2022-12345
        },
        'finding_cwe': {
            'id': 'finding_cwe_name',
            'object_type': 'FINDING',
            'data_type' : 'CWE',
            'validation_type': None,
            'input_blanks': False,
            'path': ['common_identifiers', 'CWE', 'INDEX'] # document number i.e. 501
        },
        # ASSET INFO
        'asset_multi_name': {
            'id': 'asset_multi_name',
            'object_type': 'MULTI_ASSET',
            'data_type' : 'MULTI_ASSET',
            'validation_type': None,
            'input_blanks': False,
            'path': ['asset']
        },
        'asset_name': {
            'id': 'asset_name',
            'object_type': 'ASSET',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['asset']
        },
        'asset_criticality': {
            'id': 'asset_criticality',
            'object_type': 'ASSET',
            'data_type' : 'DETAIL',
            'validation_type': 'SEVERITY', # validate
            'input_blanks': False,
            'path': ['assetCriticality']
        },
        'asset_hostname': {
            'id': 'asset_hostname',
            'object_type': 'ASSET',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['hostname']
        },
        'asset_known_ips': {
            'id': 'asset_known_ips',
            'object_type': 'ASSET',
            'data_type' : 'LIST',
            'validation_type': None,
            'input_blanks': False,
            'path': ['knownIps']
        },
        'asset_tag': {
            'id': 'asset_tag',
            'object_type': 'ASSET',
            'data_type' : 'TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        'asset_multi_tag': {
            'id': 'asset_multi_tag',
            'object_type': 'ASSET',
            'data_type' : 'MULTI_TAG',
            'validation_type': None,
            'input_blanks': False,
            'path': ['tags']
        },
        # AFFECTED ASSET INFO
        'asset_status': {
            'id': 'asset_status',
            'object_type': 'AFFECTED_ASSET',
            'data_type' : 'DETAIL',
            'validation_type': 'STATUS', # validate
            'input_blanks': False,
            'path': ['status']
        },
        'asset_sub_status': {
            'id': 'asset_sub_status',
            'object_type': 'AFFECTED_ASSET',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['subStatus']
        },
        'asset_ports': {
            'id': 'asset_ports',
            'object_type': 'AFFECTED_ASSET',
            'data_type' : 'PORTS',
            'validation_type': None,
            'input_blanks': False,
            'path': ['ports']
        },
        'asset_location_url': {
            'id': 'asset_location_url',
            'object_type': 'AFFECTED_ASSET',
            'data_type' : 'DETAIL',
            'validation_type': None,
            'input_blanks': False,
            'path': ['locationUrl']
        }
    }
    #--- END CSV---


    #--- CLIENT - template of client object - list of clients generated while running the script---

    # you can add data here that should be added to all clients
    client_template = { # need all arrays build out to prevent KEY ERR when adding data
        "sid": None,
        "name": f'Custom CSV Import Blank',
        "tags": ["custom_csv_import"],
        "description": "Client for custom csv import script findings. This Client was created because there was no client_name key mapped in the data to be imported.",
        "assets": [],
        "reports": []
    }

    clients = {}
    #--- END CLIENT---


    #--- REPORT - template of report object - list of reports generated while running the script---

    # you can add data here that should be added to all reports
    report_template = { # need all arrays build out to prevent KEY ERR when adding data
        'sid': None,
        'client_sid': None,
        "name": f'Report',
        "status": "Published",
        "tags": ["custom_csv_import"],
        "custom_field": [],
        "start_date": None,
        "end_date": None,
        "exec_summary": {
            "custom_fields": []
        },
        "findings": []
    }

    reports = {}
    #--- END REPORT---


    #--- FINDING - template of finding object - list of findings generated while running the script---

    # you can add data here that should be added to all findings
    finding_template = { # need all arrays build out to prevent KEY ERR when adding data
        'sid': None,
        'client_sid': None,
        'report_sid': None,
        'affected_asset_sid': None,
        'title': None,
        'severity': "Informational",
        'status': "Open",
        'description': "",
        'recommendations': "",
        'references': "",
        'fields': {},
        'risk_score': {
            'CVSS3_1': {
                'overall': 0,
                'vector': ""
            }
        },
        'common_identifiers': {
            "CVE": [],
            "CWE": []
        },
        'tags': ["custom_csv_import"],
        'affected_assets': {},
        'assets': []
    }

    findings = {}
    #--- END FINDING---


    #--- ASSET - template of asset object - list of assets generated while running the script---

     # you can add data here that should be added to all assets
    asset_template = { # need all arrays build out to prevent KEY ERR when adding data
        'sid': None,
        'client_sid': None,
        'finding_sid': None,
        'original_asset_sid': None,
        'is_multi': False,
        'asset': None,
        'assetCriticality': None,
        'hostname': "",
        'knownIps': [],
        'tags': ["custom_csv_import"]
    }

    # template for created nested affected asset
    affected_asset_fields = {
        'status': "Open",
        'ports': {},
        'locationUrl': "",
        'vulnerableParameters': [],
        'notes': ""
    }

    assets = {}
    affected_assets = {}
    #--- END Asset---


    # information about different states the script can run into
    log_messages = {
        'NO_CLIENT_DESIGNATION': {
            'name': "no_client_designation",
            'type': "error - skipped",
            'message': "findings were missing or had invalid data for the csv column regarding which client the finding belongs and were not added to Plextrac",
            'num': 0
        },
        'NO_CLIENT_CREATED': {
            'name': "no_client_created",
            'type': "error - skipped",
            'message': "findings had an issue when trying to create a Client, despite having valid data in the csv column regarding which client the findings belong, and were not added to Plextrac",
            'num': 0
        },
        'NO_REPORT_DESIGNATION': {
            'name': "no_report_designation",
            'type': "error - skipped",
            'message': "findings were missing or had invalid data for the csv column regarding which report the findings belong and were not added to Plextrac",
            'num': 0
        },
        'NO_REPORT': {
            'name': "no_report_created",
            'type': "error - skipped",
            'message': "findings had an issue when trying to create a Report, despite having valid data in the csv column regarding which report the findings belong, and were not added to Plextrac",
            'num': 0
        },
        'NO_MATCHED_AFFECTED_ASSET': {
            'name': "no_matched_affected_asset",
            'type': "error - skipped",
            'message': "findings had an issue when trying to add an affected asset, despite having valid data in the csv column regarding the affected asset name, and were not added to Plextrac",
            'num': 0
        },
        'NO_UNMATCHED_RELATED_IT_ASSET': {
            'name': "no_unmatched_affected_asset",
            'type': "error - skipped",
            'message': "finidngs were missing or had invalid data for the csv column regarding the affected asset name and all asset information was not added to Plextrac for these findings",
            'num': 0
        },
        'NO_FINDING_CREATED': {
            'name': "no_finding_created",
            'type': "error - skipped",
            'message': "findings had an issue creating a new finding, so were not added to Plextrac",
            'num': 0
        },
        'NO_DATA_VALIDATION': {
            'name': "no_data_validation",
            'type': "exception - manual verification",
            'message': "findings had 1 or more values that did not fit within csv formulas' verification rules, these values were skipped",
            'num': 0
        },
        'SUCCESS': {
            'name': "success",
            'type': "info",
            'message': "findings were parsed and imported successfully",
            'num': 0
        }
    }


    def __init__(self):
        """
        
        """
        self.csv_headers_mapping = None
        self.csv_data = None
        self.logging_data = None
        self.parser_progess = None
        self.parser_date = time.strftime("%m/%d/%Y", time.localtime(time.time()))
        self.parser_time = time.strftime("%Y_%m_%d_%H_%M_%S", time.localtime(time.time()))

        self.client_template['name'] = f'Custom CSV Import {self.parser_date}'

        # csv logging
        self.CSV_LOGS_FILE_PATH = f'parser_logs_{self.parser_time}.csv'
        # txt logging
        self.LOGS_FILE_PATH = f'logs_{self.parser_time}.txt'
        self.log = logging
        self.log.basicConfig(
            level=self.log.INFO,
            format="%(asctime)s [%(levelname)s] %(message)s",
            handlers=[
                self.log.FileHandler(self.LOGS_FILE_PATH),
                self.log.StreamHandler()
            ]
        )



    #----------getters and setter----------
    def get_data_mapping_ids(self):
        return list(self.data_mapping.keys())
    
    def get_csv_headers(self):
        """
        Returns the list of expected based on the csv_header value in the tracker array containing data mapping info.
        """
        return list(self.csv_headers_mapping.keys())

    def get_headers_by_data_type(self, data_type):
        type_mappings = list(map(lambda x: x['id'], list((filter(lambda x: (x['data_type'] == data_type), self.data_mapping.values()))) ))
        print(type(type_mappings))
        print(type_mappings)
        # mapped_headers = filter(lambda header, id: (id in type_mappings), self.csv_headers_mapping.items())
        # print(type(mapped_headers))
        # print(mapped_headers)


    def get_key_from_header(self, header):
        return self.csv_headers_mapping.get(header)

    # only returns the first instance of the key. will not get expected return if a generic key is used i.e. finding_custom_field
    def get_header_from_key(self, key):
        for header, id in self.csv_headers_mapping.items():
            if key == id:
                return header
        return None
    #----------End getters and setter----------


    #----------logging functions----------
    def create_log_file(self):
        """
        Creates a CSv with unique file name and populates it with the data that will be parsed
        and imported into Plextrac. As the script runs, it will append logs to each entry.

        This allows the ability to to filter the log file and modify and retry parsing
        for findings that were skipped or deemed not imported correctly.
        """
        print("Creating log file...")
        try:
            with open(self.CSV_LOGS_FILE_PATH, mode='w', encoding="utf8") as file:
                writer = csv.writer(file)
                header_row = self.get_csv_headers()
                header_row.append("Parser Logs")
                writer.writerow(header_row)

                # adding findings to be parsed and imported - logs will be later added as needed to each entry
                for row in self.csv_data:
                    # fixes csv when given csv is not square shape (rows can be different lengths depending on empty cells in the last col)
                    while len(row) < len(self.get_csv_headers())+1:
                        row.append("")
                    writer.writerow(row)

                print(f'Info: Logs will be saved to \'{self.CSV_LOGS_FILE_PATH}\'')
        except Exception as e:
            print(f'Error setting up log file: {e}')


    def add_log(self, log, e=None):
        """
        While the script is parsing and adding findings it can run into 2 conditions:
        - A finding did not have the full expected data, but was added with data given (should verify the created finding is as expected)
        - A finding did not have necessary data, script cannot continue

        This function is called to add either type of message to a finding entry
        """
        i = self.parser_progess
        try:
            with open(self.CSV_LOGS_FILE_PATH, mode='r', encoding="utf8") as file:
                reader = csv.reader(file)
                temp_csv_data = []
                for row in reader:
                    temp_csv_data.append(row)

                log['num'] += 1
                new_log = f'{log["type"]}:  {log["name"]}'
                if e != None:
                    new_log = f'{new_log}\n{e}'
                temp_csv_data[i+1][len(self.data_mapping)] = f'{temp_csv_data[i+1][len(self.data_mapping)]}\n{new_log}'

            with open(self.CSV_LOGS_FILE_PATH, mode='w', encoding="utf8") as file:
                writer = csv.writer(file)
                writer.writerows(temp_csv_data)
            
        except Exception as e:
            print(f'Error updating log file: {e}')

    
    def display_parser_results(self):
        print(f'\n\nImport completed!') # Successfully imported {self.log_messages["SUCCESS"]["num"]}/{len(self.csv_data)} findings.\n')
        
        # for log in self.log_messages.values():
        #     if log['num'] > 0:

        #         print(f'{log["num"]} {log["message"]}.')

        print(f'\nDetailed logs can be found in \'{self.LOGS_FILE_PATH}\'')
    #----------End logging functions----------


    #----------Post parsing handling functions----------
    def handle_finding_dup_names(self):
        """
        Runs through all findings and updates the titles for any duplicates.
        Cannot be done during parsing since we still have to look for duplicates there
        """
        for f in self.findings.values():
            if f['dup_num'] > 1:
                f['title'] = f'{f["title"]} ({f["dup_num"]})'
            f.pop("dup_num")


    def add_asset_to_finding(self, finding, asset, finding_sid, asset_sid):
        """
        Adds the asset data as an affected asset on a finding.
        Must be called after the finding and asset are created
        """
        asset_id = asset['id']
        # asset wasn't created successfully, can't add
        if asset_id == None:
            return finding

        affected_asset = asset
        affected_asset_fields = deepcopy(self.affected_asset_fields)

        # single asset with possible affected asset fields
        if self.assets[asset_sid]['is_multi'] == False:
            affected_asset_fields = self.affected_assets[self.findings[finding_sid]['affected_asset_sid']]
        
        affected_asset.update(affected_asset_fields)
        finding['affected_assets'][asset_id] = affected_asset

        return finding
    #----------End post parsing handling functions----------


    #----------Object Handling----------
    def handle_client(self, row):
        """
        Returns a client sid and name based on the csv columns specified that relate to client data.

        Looks through list of clients already created during this running instance of the script
        Determines if a client exists that the current entry should be added to

        Returns the client sid and name of exisitng client or
        Creates new client and adds all csv column data that relates to the client
        """
        matching_clients = []

        # filter for matching clients
        header = self.get_header_from_key("client_name")
        if header == None:
            matching_clients = list(filter(lambda x: (f'Custom CSV Import {self.parser_date}' == str(x['name'])), self.clients.values()))
        else:
            index = list(self.csv_headers_mapping.keys()).index(header)
            value = row[index]

            matching_clients = list(filter(lambda x: (str(value) in str(x['name'])), self.clients.values()))

        # return matched client
        if len(matching_clients) > 0:
            client = matching_clients[0]
            self.log.info(f'INFO: Found existing client {client["name"]}')
            return client['sid'], client['name']

        # return new client
        self.log.info(f'INFO: No client found. Creating new client...')
        new_sid = uuid4()
        client = deepcopy(self.client_template)
        client['sid'] = new_sid

        self.add_data_to_object(client, "CLIENT", row)

        self.clients[new_sid] = client

        return new_sid, client['name']


    def handle_report(self, row, client_sid):
        """
        Returns a report sid and name based the csv columns specified that relate to report data.

        Looks through list of reports already created during this running instance of the script for the given client
        Determines if a report exists that the current entry should be added to

        Returns the report sid and name of exisitng report or
        Creates new report and adds all csv column data that relates to the report
        """
        matching_reports = []

        # filter for matching reports
        header = self.get_header_from_key("report_name")
        if header == None:
            matching_reports = self.reports.values()
            matching_reports = filter(lambda x: (x['client_sid'] == client_sid), matching_reports)
            matching_reports = list(filter(lambda x: ("Report" in str(x['name'])), matching_reports))
        else:
            index = list(self.csv_headers_mapping.keys()).index(header)
            value = row[index]

            matching_reports = self.reports.values()
            matching_reports = filter(lambda x: (x['client_sid'] == client_sid), matching_reports)
            matching_reports = list(filter(lambda x: (str(value) in str(x['name'])), matching_reports))

        # return matched report
        if len(matching_reports) > 0:
            report = matching_reports[0]
            self.log.info(f'INFO: Found existing report {report["name"]}')
            return report['sid'], report['name']

        # return new report
        self.log.info(f'INFO: No report found. Creating new report...')
        new_sid = uuid4()
        report = deepcopy(self.report_template)
        report['sid'] = new_sid
        report['client_sid'] = client_sid

        self.add_data_to_object(report, "REPORT", row)

        self.reports[new_sid] = report
        self.clients[client_sid]['reports'].append(new_sid)

        return new_sid, report['name']


    def handle_finding(self, row, client_sid, report_sid):
        """
        Returns a finding sid and name based the csv columns specified that relate to finding data.

        Looks through list of findings already created during this running instance of the script for the given client and report
        Determines if a finding has a duplicate and needs a different finding title

        Creates new finding and adds all csv column data that relates to the finding

        Returns the finding sid and name of the new finding
        """
        matching_findings = list(self.findings.values())
        matching_findings = filter(lambda x: (x['client_sid'] == client_sid), matching_findings)
        matching_findings = filter(lambda x: (x['report_sid'] == report_sid), matching_findings)

        # filter for matching findings by title
        header = self.get_header_from_key('finding_title')

        index = list(self.csv_headers_mapping.keys()).index(header)
        value = row[index]

        matching_findings = list(filter(lambda x: (value == x['title']), matching_findings))

        # return finding
        new_sid = uuid4()
        finding = deepcopy(self.finding_template)
        finding['sid'] = new_sid
        finding['client_sid'] = client_sid
        finding['report_sid'] = report_sid
        finding['dup_num'] = len(matching_findings) + 1

        self.add_data_to_object(finding, "FINDING", row)

        self.findings[new_sid] = finding
        self.reports[report_sid]['findings'].append(new_sid)

        return new_sid, finding['title']


    def handle_multi_asset(self, row, client_sid, finding_sid):
        """
        Creates an asset for each asset name listed in the asset_multi_name column.

        Looks through list of assets already created during this running instance of the script for the given client
        Determines if an asset has a duplicate, but will create a neww asset with the same name

        Does NOT add any other asset data keys besides the names.
        """
        matching_assets = list(self.assets.values())
        matching_assets = filter(lambda x: (x['client_sid'] == client_sid), matching_assets)

        header = self.get_header_from_key('asset_multi_name')
        if header == None:
            return

        index = list(self.csv_headers_mapping.keys()).index(header)
        value = row[index]
        if value == "":
            return

        for asset_name in value.split(","):
            asset_name = asset_name.strip()
            temp_matching_assets = list(filter(lambda x: (asset_name == x['asset']), matching_assets))

            # create asset
            new_sid = uuid4()
            asset = deepcopy(self.asset_template)
            asset['sid'] = new_sid
            asset['client_sid'] = client_sid
            asset['dup_num'] = len(temp_matching_assets) + 1
            if len(temp_matching_assets) > 0:
                asset['original_asset_sid'] = temp_matching_assets[0]['sid']

            self.set_value(asset, ['asset'], asset_name)
            asset.update(deepcopy(self.affected_asset_fields))
            asset['is_multi'] = True

            self.assets[new_sid] = asset
            self.clients[client_sid]['assets'].append(new_sid)
            self.findings[finding_sid]['assets'].append(new_sid)


    def handle_asset(self, row, client_sid, finding_sid):
        """
        Returns an asset sid and name based the csv columns specified that relate to asset data.

        Looks through list of assets already created during this running instance of the script for the given client
        Determines if an asset has a duplicate, but will create a neww asset with the same name

        Creates new asset and adds all csv column data that relates to the asset

        Returns the asset sid and name of the new asset
        """
        matching_assets = list(self.assets.values())
        matching_assets = filter(lambda x: (x['client_sid'] == client_sid), matching_assets)

        header = self.get_header_from_key('asset_name')
        if header == None:
            return None, None

        index = list(self.csv_headers_mapping.keys()).index(header)
        value = row[index]
        if value == "":
            return None, None

        matching_assets = list(filter(lambda x: (value == x['asset']), matching_assets))

        # return asset
        new_sid = uuid4()
        asset = deepcopy(self.asset_template)
        asset['sid'] = new_sid
        asset['client_sid'] = client_sid
        asset['dup_num'] = len(matching_assets) + 1
        if len(matching_assets) > 0:
            asset['original_asset_sid'] = matching_assets[0]['sid']

        self.add_data_to_object(asset, "ASSET", row)

        self.assets[new_sid] = asset
        self.clients[client_sid]['assets'].append(new_sid)
        self.findings[finding_sid]['assets'].append(new_sid)

        return new_sid, asset['asset']

    
    def handle_affected_asset(self, row, finding_sid):
        """
        Handles affected asset data that relates to an asset that should be added on a finding

        Creates new affected_asset and adds all csv column data that relates to the affected_asset
        """
        new_sid = uuid4()
        affected_asset = deepcopy(self.affected_asset_fields)

        self.add_data_to_object(affected_asset, "AFFECTED_ASSET", row)

        self.affected_assets[new_sid] = affected_asset
        self.findings[finding_sid]['affected_asset_sid'] = new_sid
    #----------End Object Handling----------


    #----------functions to add specific types of data to certain locations----------
    def set_value(self, obj, path, value):
        if len(path) == 1:
            if path[0] == "INDEX":
                obj.append(value)
            else:    
                obj[path[0]] = value
            return

        if path[0] == "INDEX":
            obj.append({})
            self.set_value(obj[-1], path[1:], value)
        else:
            self.set_value(obj[path[0]], path[1:], value)

    # detail
    def add_detail(self, header, obj, mapping, value):
        path = mapping['path']

        if mapping['validation_type'] == "DATE_ZULU":
            raw_date = utils.try_parsing_date(self.log, value, header)
            if raw_date != None:
                self.set_value(obj, path, time.strftime("%Y-%m-%dT08:00:00.000000Z", raw_date))
                return

        if mapping['validation_type'] == "DATE_EPOCH":
            raw_date = utils.try_parsing_date(self.log, value, header)
            if raw_date != None:
                self.set_value(obj, path, int(time.mktime(raw_date)*1000))
                return

        if mapping['validation_type'] == "SEVERITY":
            severities = ["Critical", "High", "Medium", "Low", "Informational"]
            if value not in severities:
                self.log.exception(f'Header "{header}" value "{value}" is not a valid severity. Must be in the list ["Critical", "High", "Medium", "Low", "Informational"] Skipping...')
                return

        if mapping['validation_type'] == "STATUS":
            statuses = ["Open", "In Process", "Closed"]
            if value not in statuses:
                self.log.exception(f'Header "{header}" value "{value}" is not a valid status. Must be in the list ["Open", "In Process", "Closed"] Skipping...')
                return

        if mapping['validation_type'] == "ASSET_TYPE":
            types = ["Workstation", "Server", "Network Device", "Application", "General"]
            if value not in types:
                self.log.exception(f'Header "{header}" value "{value}" is not a valid asset type. Must be in the list ["Workstation", "Server", "Network Device", "Application", "General"] Skipping...')
                return

        if mapping['validation_type'] == "FLOAT":
            try:
                self.set_value(obj, path, float(value))
            except ValueError:
                self.log.exception(f'Header "{header}" value "{value}" is not a valid number. Skipping...')
            return

        if mapping['validation_type'] == "BOOL":
            try:
                self.set_value(obj, path, bool(value))
            except ValueError:
                self.log.exception(f'Header "{header}" value "{value}" cannot be converted to a boolean. Skipping...')
            return
        
        self.set_value(obj, path, str(value))

    # client/report custom field
    def add_label_value(self, header, obj, mapping, value):
        label_value = {
            'label': header.strip(),
            'value': value
        }

        self.set_value(obj, mapping['path'], label_value)

    # finding custom field
    def add_key_label_value(self, header, obj, mapping, value):
        path = copy(mapping['path'])
        path.append(utils.format_key(header.strip()))

        label_value = {
            'label': header.strip(),
            'value': value
        }

        self.set_value(obj, path, label_value)

    # tag
    def add_tag(self, header, obj, mapping, value):
        utils.add_tag(obj['tags'], value)

    # multiple tags
    def add_tag(self, header, obj, mapping, value):
        tags = value.split(",")
        for tag in tags:
            utils.add_tag(obj['tags'], value.strip())

    # report narrative
    def add_label_text(self, header, obj, mapping, value):
        label_text = {
            'label': header.strip(),
            'text': value
        }

        self.set_value(obj, mapping['path'], label_text)

    # finding cve
    def add_cve(self, header, obj, mapping, value):
        cves = value.split(",")
        for cve in cves:
            values = cve.strip().split("-")
            try:
                data= {
                    "name": "value",
                    "year": int(values[1]),
                    "id": int(values[2]),
                    "link": f'https://www.cve.org/CVERecord?id={value}'
                }

                self.set_value(obj, mapping['path'], data)
            except ValueError:
                self.log.exception(f'Header "{header}" value "{value}" is not a list of valid CVE IDs. Expects "CVE-2022-12345" or "CVE-2022-12345, CVE-2022-67890" Skipping...')

    # finding cwe
    def add_cwe(self, header, obj, mapping, value):
        cwes = value.split(",")
        for cwe in cwes:
            cwe = cwe.strip()
            try:
                data = {
                    "name": f'CWE-{cwe}',
                    "id": int(cwe),
                    "link": f'https://cwe.mitre.org/data/definitions/{cwe}.html'
                }

                self.set_value(obj, mapping['path'], data)
            except ValueError:
                self.log.exception(f'Header "{header}" value "{value}" is not a list of valid CWE numbers. Expects "123" or "123, 456" Skipping...')

    # list (asset known ips, operating systems)
    def add_list(self, header, obj, mapping, value):
        if value not in obj[mapping['path'][0]]:
            obj[mapping['path'][0]].append(value)

    # asset port obj - csv data should be formatted "port|service|protocol|version"
    def add_port(self, header, obj, mapping, value):
        ports = value.split(",")
        for port in ports:
            data = port.strip().split("|")
            if len(data) != 4:
                print(f'WARN: Port data {port} not formatted correctly. Expected "port|service|protocol|version". Ignoring...')
                return
            if data[0] == "":
                print(f'WARN: Missing port number. Expected "port|service|protocol|version". Ignoring...')
                return
            port = {
                'number': data[0].strip(),
                'service': data[1].strip(),
                'protocol': data[2].strip(),
                'version': data[3].strip()
            }
            obj['ports'][data[0]] = port
    #----------end functions----------


    def add_data_to_object(self, obj, obj_type, row):
        """
        Controller to add different types of data to different locations on an object.

        Objects can be clients, reports, findings, assets, affected assets, or vulnerabilities

        Adds all data from csv row that coresponds to the object type
        """
        for index, header in enumerate(self.csv_headers_mapping):
            data_mapping_key = self.get_key_from_header(header)
            if data_mapping_key == None:
                self.log.debug(f'CSV header "{header}" not mapped with a location key. Skipping {header}...')
                continue

            data_mapping = self.data_mapping.get(data_mapping_key)
            if data_mapping == None:
                self.log.exception(f'No Plextrac mapping for <{data_mapping_key}>, was it typed incorrectly? Ignoring...')
                continue

            # only loop through the field for hte correct obj type
            if data_mapping['object_type'] != obj_type:
                continue

            data_type = data_mapping['data_type']
            value = row[index]

            # determine whether to add blank values
            if data_mapping['input_blanks'] or value != "":

                if data_type == "DETAIL":
                    self.add_detail(header, obj, data_mapping, value)
                elif data_type == "CUSTOM_FIELD":
                    self.add_label_value(header, obj, data_mapping, value)
                elif data_type == "KEY_CUSTOM_FIELD":
                    self.add_key_label_value(header, obj, data_mapping, value)
                elif data_type == "TAG":
                    self.add_tag(header, obj, data_mapping, value)
                elif data_type == "MULTI_TAG":
                    self.add_multi_tag(header, obj, data_mapping, value)
                elif data_type == "NARRATIVE":
                    self.add_label_text(header, obj, data_mapping, value)
                elif data_type == "CVE":
                    self.add_cve(header, obj, data_mapping, value)
                elif data_type == "CWE":
                    self.add_cwe(header, obj, data_mapping, value)
                elif data_type == "LIST":
                    self.add_list(header, obj, data_mapping, value)
                elif data_type == "PORTS":
                    self.add_port(header, obj, data_mapping, value)


    def parser_row(self, row):
        """
        Parsers the csv row to determine which client and report the finding should be added to.

        Gets or creates client to import to
        Gets or creates report to import to
        Creates finding
        Creates asset
        """
        # query csv row for client specific info and create or choose client
        client_sid, client_name = self.handle_client(row)
        if client_sid == None:
            return

        # query csv row for report specific data and creaate or choose report
        report_sid, report_name = self.handle_report(row, client_sid)   
        if report_sid == None:
            return     
        
        # query csv row for finding specific data and create finding
        finding_sid, finding_name = self.handle_finding(row, client_sid, report_sid)
        if finding_sid == None:
            return

        self.handle_multi_asset(row, client_sid, finding_sid)

        # query csv row for asset specific data and create or choose asset
        asset_sid, asset_name = self.handle_asset(row, client_sid, finding_sid)

        # if there was a header mapped to a single asset, handle the potential affected asset data for the single asset
        if finding_sid != None and asset_sid != None:
            self.handle_affected_asset(row, finding_sid)

    def parse_data(self):
        """
        Top level parsing controller. Loops through loaded csv, gathers required data, calls function to process data.

        Creates and sets up csv logging file
        Determine where to look for finding name (needed to verify each row contains a finding)
        Loop through csv findings
        - Verfiy row contains finding
        - Call to process finding
        """
        # self.create_log_file()

        # get index of 'name' obj in self.data_mapping - this will be the index to point us to the name column in the csv
        try:
            csv_finding_title_index = list(self.csv_headers_mapping.values()).index('finding_title')
        except ValueError:
            self.log.critical(f'Did not map "finding_title" key to any csv headers. Cannot process CSV. Exiting...')
            exit()

        print(f'---Beginning CSV parsing---')
        self.parser_progess = 0
        for row in self.csv_data:
            self.log.info(f'=======Parsing Finding {self.parser_progess+1}=======')

            # checking if current row contains a finding since the csv could have rows that extend beyond finding data
            if row[csv_finding_title_index] == "":
                self.log.info(f'Row {self.parser_progess+2} in the CSV did not have a value for the finding_title. Skipping...')
                continue
            
            vuln_name = row[csv_finding_title_index]
            self.log.info(f'---{vuln_name}---')
            self.parser_row(row)

            self.parser_progess += 1
            self.log.info(f'=======End {vuln_name}=======')

            # if self.parser_progess == 150:
            #     break

        # post parsing processing
        print(f'\n---Post parsing proccessing---')
        self.handle_finding_dup_names()


    def import_data(self, auth):
        """
        Calls Plextrac's API to creates new clients, reports and add findings and assets
        """
        # send API creation requests to Plextrac
        print(f'\n---Importing data---')
        # clients
        for client in self.clients.values():
            payload = deepcopy(client)
            payload.pop("assets")
            payload.pop("reports")
            payload.pop("sid")
            self.log.info(f'INFO: Creating client <{payload["name"]}>')
            response = request_create_client(auth.base_url, auth.get_auth_headers(), payload)
            if response.get("status") != "success":
                self.log.error(f'ERR: Could not create client. Skipping all reports and findings under this client...')
                continue
            self.log.info(f'Successfully created client!')
            client_id = response.get("client_id")

            # client assets
            for asset_sid in client['assets']:
                asset = self.assets[asset_sid]
                if asset['original_asset_sid'] != None:
                    self.log.info(f'INFO: Found existing asset <{asset["asset"]}>')
                    asset['asset_id'] = self.assets[asset['original_asset_sid']]['asset_id']
                    continue

                payload = deepcopy(asset)
                payload.pop("sid")
                payload.pop("client_sid")
                payload.pop("finding_sid")
                payload.pop("dup_num")
                payload.pop("is_multi")
                self.log.info(f'INFO: Creating asset <{payload["asset"]}>')
                response = request_create_asset(auth.base_url, auth.get_auth_headers(), payload, client_id)
                if response.get("message") != "success":
                    self.log.error(f'ERR: Could not create asset. Skipping...')
                    continue
                self.log.info(f'Successfully created asset!')
                asset['asset_id'] = response.get("id")

            # reports
            for report_sid in client['reports']:
                payload = deepcopy(self.reports[report_sid])
                payload.pop("findings")
                payload.pop("sid")
                payload.pop("client_sid")
                self.log.info(f'INFO: Creating report <{payload["name"]}>')
                response = request_create_report(auth.base_url, auth.get_auth_headers(), payload, client_id)
                if response.get("message") != "success":
                    self.log.error(f'ERR: Could not create report. Skipping all findings under this report...')
                    continue
                self.log.info(f'Successfully created report!')
                report_id = response.get("report_id")

                # findings
                for finding_sid in self.reports[report_sid]['findings']:
                    finding = self.findings[finding_sid]
                    payload = deepcopy(finding)
                    payload.pop("assets")
                    payload.pop("sid")
                    payload.pop("client_sid")
                    payload.pop("report_sid")
                    payload.pop("affected_asset_sid")
                    self.log.info(f'INFO: Creating finding <{payload["title"]}>')
                    response = request_create_finding(auth.base_url, auth.get_auth_headers(), payload, client_id, report_id)
                    if response.get("message") != "success":
                        self.log.error(f'ERR: Could not create finding. Skipping...')
                        continue
                    self.log.info(f'Successfully created finding!')
                    finding_id = response.get("flaw_id")

                    # update finding with asset info
                    if len(finding['assets']) > 0:
                    
                        pt_finding = request_get_finding(auth.base_url, auth.get_auth_headers(), client_id, report_id, finding_id)

                        for asset_sid in finding['assets']:
                            pt_asset = request_get_asset(auth.base_url, auth.get_auth_headers(), client_id, self.assets[asset_sid]['asset_id'])
                            pt_finding = self.add_asset_to_finding(pt_finding, pt_asset, finding_sid, asset_sid)
                    
                        self.log.info(f'INFO: Updating finding <{pt_finding["title"]}> with asset information')
                        response = request_update_finding(auth.base_url, auth.get_auth_headers(), pt_finding, client_id, report_id, finding_id)
                        if response.get("message") != "success":
                            self.log.error(f'ERR: Could not update finding. Skipping...')
                            continue
                        self.log.info(f'Successfully added asset info to finding!')
