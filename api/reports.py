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

def get_report_list(base_url, headers, payload):
    """
    This request **retrieves a list of reports** for a tenant.

`pagination` is a required key while `sort` and `filters` are optional.

The `pagination.limit` must be one of \[5, 10, 25, 50, 100, 1000\]. The `pagination.offset` is the number of records to shift by, not the number of pages to shift by. i.e. offset 2, limit 10 gives you records 2-12 not 20-30

The following values can be used in the `filters.by` field:

- name
- reviewers (array of reviewer emails)
- operators(array of operator emails)
- clients (array of client IDs a report is under)
- status (array of report statuses)
    

The following values can be used in the `sort.by` field:

- name
- status
    

The following values can be used in the `sort.order` field:

- ASC
- DESC
    """
    name = "Get Report List"
    root = "/api/v2"
    path = f'/reports'
    return request.post(base_url, headers, root+path, name, payload)

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

def bulk_delete_reports(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Bulk Delete Reports"
    root = "/api/v2"
    path = f'/reports/bulk/delete'
    return request.post(base_url, headers, root+path, name, payload)

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

def bulk_add_tags_to_report(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Bulk Add Tags to Report"
    root = "/api/v2"
    path = f'/reports/bulk/tags'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_assign_reviewers_to_report(base_url, headers, payload):
    """
    The reviewer email must match an existing PT user email.
    """
    name = "Bulk Assign Reviewers to Report"
    root = "/api/v2"
    path = f'/reports/bulk/reviewers'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_adjust_status_of_report(base_url, headers, payload):
    """
    The reviewer email must match an existing PT user email.
    """
    name = "Bulk Adjust Status of Report"
    root = "/api/v2"
    path = f'/reports/bulk/status'
    return request.post(base_url, headers, root+path, name, payload)

def export_report_to_ptrac(base_url, headers, clientId, reportId):
    """
    This request **exports a report** in ptrac format for further manipulation and future importing back into PlexTrac.

The `instanceUrl` ,`clientId,` and `reportId` is needed to execute.
    """
    name = "Export Report to Ptrac"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/export/ptrac'
    return request.get(base_url, headers, root+path, name)

def export_report_to_word(base_url, headers, clientId, reportId, includeEvidence, templateID):
    """
    This requests **exports a PlexTrac** **report to Word** (.docx).

**Important**: Be aware that setting `includeEvidence` to `true` will result in long export times due to handling extra data. Set to `false` unless evidence is required at export.

The endpoint needs the report data and Jinja2 coded Word .docx file (Export Template) that will be populated with data.

If the Report Template field in a report is selected, that report already has a reference to the Jinja2 Export Template. If not, add the additional `templateID` query parameter. This is the ID of a previously uploaded Export Template. See the LIst Export Templates endpoing for more info about retrieving this ID.

More information on [exporting a report]() can be found on the PlexTrac Product Documentation site.

    Query Parameters:
    includeEvidence: Include Raw Evidence in Export - example (false)
    templateID: existing Export Template ID - example ({{exportTemplateId}})
    """
    name = "Export Report to Word"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/export/doc?includeEvidence={includeEvidence}?templateID={templateID}'
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
