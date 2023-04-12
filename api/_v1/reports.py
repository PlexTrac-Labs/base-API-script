from utils import request_handler as request

def list_client_reports(base_url, headers, clientId):
    """
    This request **retrieves** a list of reports for a specific client. The information retrieved is limited and intended to provide an overview of the number of reports for a client.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| id | report ID and client ID combined | report_500004_client_4155 |
| doc_id | client ID | 4155 |
| data | information about the report, including report id, report name, and report status | 500004, Karbo Industries, draft |
    """
    name = "List Client Reports"
    root = "/api/v1"
    path = f'/client/{clientId}/reports'
    return request.get(base_url, headers, root+path, name)

def get_report(base_url, headers, clientId, reportId, payload):
    """
    This request **retrieves** a specific report for a client and provides robust information about the report.

The `instanceUrl`, `reportId,` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| name | report name | Karbo Pentest Results May 2022 |
| status | report status | draft |
| includeEvidence |  | false |
| report_id | report ID | 500004 |
| doc_type | document type | report |
| report_Type | report template type | default |
| tags | any associated tags with the report | pentest, 2022 |
| custom_field | any custom fields associated with the report seprated by a label and value | Custom Field  <br>sample value |
| template | report template used | 754b-4289-8b5a-684391d5b988 |
| start_date | date and time report started | 2022-05-17T19:00:11.146Z |
| end_date | date and time report ended | 2022-05-18T19:00:13.168Z |
| fields_template |  | 7c76e35c-1dfc-4623-8dc4-3a0bd33658a8 |
| exec_summary | list of report narratives custom fields, IDs, labels and text |  |
    """
    name = "Get Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}'
    return request.get(base_url, headers, root+path, name, payload)

def create_report(base_url, headers, clientId, payload):
    """
    This request **creates** a report for a client. The request body should contain a JSON that represents the report to be created.

This JSON has the properties of 'name' and 'status'.

*name (string) - name of the report*

The `instanceUrl`and `clientId` is needed to execute.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| message | status of task | success |
| doc_id | new report ID combined with client ID | report_500006_client_4155 |
| report_id | report ID | 500006 |
    """
    name = "Create Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/create'
    return request.post(base_url, headers, root+path, name, payload)

def update_report(base_url, headers, clientId, reportId, payload):
    """
    This request **updates** a report's `name`, `description`, `logistics`, `status`, `template`, `start_date`, `end_date`, and `fields template`.

The `instanceUrl`, `reportId,` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | status of change update | success |
| message | change message | Report Updated Successfully |
| data | contains all the data updated |  |
| template | report template used | 754b-4289-8b5a-684391d5b988 |
| start_date | date and time report started | 2022-05-17T19:00:11.146Z |
| end_date | date and time report ended | 2022-05-18T19:00:13.168Z |
| fields_template |  | 7c76e35c-1dfc-4623-8dc4-3a0bd33658a8 |
| report_id | report ID | 500004 |
| client_id | client ID | 4155 |
| doc_type | document type | report |
    """
    name = "Update Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_report(base_url, headers, clientId, reportId):
    """
    This request **removes** a report for a client.

The `instanceUrl` ,`clientId,` and `reportId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| data | further validation | true |
    """
    name = "Delete Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}'
    return request.delete(base_url, headers, root+path, name)

def get_exhibit(base_url, headers, clientId, reportId, exhibitId):
    """
    This request **retrieves** an exhibit filename from a specific report.

The `instanceUrl` ,`clientId,` `reportId,` and `exhibitId` is needed to execute.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| id | filename of exhibit | 2430ffd3-0c48-4adf-b211-d960ed06176d.png |
    """
    name = "Get Exhibit"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/{exhibitId}'
    return request.get(base_url, headers, root+path, name)

def export_report_to_ptrac(base_url, headers, clientId, reportId):
    """
    This request **exports a report** in ptrac format for further manipulation and future importing back into PlexTrac.

The `instanceUrl` ,`clientId,` and `reportId` is needed to execute.
    """
    name = "Export Report to Ptrac"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/export/ptrac'
    return request.get(base_url, headers, root+path, name)

def import_ptrac_report(base_url, headers, clientId, payload):
    """
    No description in Postman
    """
    name = "Import Ptrac Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/import'
    return request.post(base_url, headers, root+path, name, payload)

def import_findings(base_url, headers, clientId, reportId, source):
    """
    No description in Postman
    """
    name = "Import Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/{source}'
    return request.post(base_url, headers, root+path, name)
