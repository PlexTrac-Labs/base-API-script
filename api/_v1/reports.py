from utils import request_handler as request

def list_client_reports(base_url, headers, clientId):
    """
    This request **retrieves** a list of reports for a specific client. The information retrieved is limited and intended to provide an overview of the number of reports for a client.

The `instanceUrl` and `clientId` is needed to execute the call.

A successful call returns a List of JSON objects with summarized information about each report.

Below is the structure of the summarized JSON returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| id | report ID and client ID combined | report_500004_client_4155 |
| doc_id | List with a single value of client ID | \[4155\] |
| data | List of information about the report:  <br>report id  <br>report name  <br>null value  <br>report status  <br>number of findings  <br>List of operators  <br>List of reviewers  <br>epoch milliseconds of report creation date  <br> | \[500004, "Karbo Industries", null, "Draft", 1, \["test.operator@email.com"\], \["test.reviewer@email.com"\], 1680796600582\]  <br> |
    """
    name = "List Client Reports"
    root = "/api/v1"
    path = f'/client/{clientId}/reports'
    return request.get(base_url, headers, root+path, name)

def get_report(base_url, headers, clientId, reportId, payload):
    """
    This request **retrieves** a specific report for a client and provides robust information about the report.

The `instanceUrl`, `reportId,` and `clientId` is needed to execute the call.

A successful call returns the JSON object of the report stored in the DB. See [Report Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object) for details on how this JSON is structured
    """
    name = "Get Report"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}'
    return request.get(base_url, headers, root+path, name, payload)

def create_report(base_url, headers, clientId, payload):
    """
    This request **creates** a report for a client.

The `instanceUrl`and `clientId` is needed to execute.

In addition to the example below, see [Report Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object) for details on the payload structure.

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
    This request **updates** a report. This does not update/relate to the findings on a report.

The `instanceUrl`, `reportId,` and `clientId` is needed to execute the call.

In addition to the example below, see [Report Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/report-object) for details on the payload structure.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | status of change update | success |
| message | change message | Report Updated Successfully |
| data | the JSON of the updated report stored in the DB |  |
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
