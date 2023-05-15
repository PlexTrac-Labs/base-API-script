from utils import request_handler as request

def list_writeups(base_url, headers):
    """
    This request retrieves **all** WriteupsDB entries for a tenant.

The `instanceUrl` is needed to execute the call.

Below is a list of the information that will be returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| description | summary of writeup | The application responds to login submissions with a link containing the user's password within the URL query string. |
| doc_id | document ID | 104560 |
| doc_type | document type | template |
| id | template ID | template_104560 |
| recommendations | writeup recommendation | The application should never transmit any sensitive information within the URL query string. There is no good reason for a login mechanism to echo passwords back to the user, and the mechanism should be modified to remove this behavior. |
| references | writeup references | CWE-598: Information Exposure Through Query Strings in GET Request |
| repositoryId | repository ID | cl0e3lc0c002318m |
| severity | writeup severity value |  |
| source | writeup source | Burp |
| tenantId | tenant ID that writeup exists under | 40632 |
| title | writeup title | Password returned in URL query string |
    """
    name = "List Writeups"
    root = "/api/v1"
    path = f'/template/list'
    return request.get(base_url, headers, root+path, name)

def get_writeups(base_url, headers, writeupId):
    """
    This request retrieves **a defined** writeup.

The `instanceUrl` is needed to execute the call.

Below is a list of the information that will be returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| description | summary of writeup | The application responds to login submissions with a link containing the user's password within the URL query string. |
| doc_id | document ID | 104560 |
| doc_type | document type | template |
| id | template ID | template_104560 |
| recommendations | writeup recommendation | The application should never transmit any sensitive information within the URL query string. There is no good reason for a login mechanism to echo passwords back to the user, and the mechanism should be modified to remove this behavior. |
| references | writeup references | CWE-598: Information Exposure Through Query Strings in GET Request |
| repositoryId | repository ID | cl0e3lc0c002318m |
| severity | writeup severity value |  |
| source | writeup source | Burp |
| tenantId | tenant ID that writeup exists under | 40632 |
| title | writeup title | Password returned in URL query string |
    """
    name = "Get Writeups"
    root = "/api/v1"
    path = f'/template/{writeupId}'
    return request.get(base_url, headers, root+path, name)

def create_writeups(base_url, headers, payload):
    """
    This request **adds a new** writeup to a specific repository.

The `instanceUrl` is needed to execute the call.

Below is a list of information needed to fulfil the request.

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| title | title of writeup | The application responds to login submissions with a link containing the user's password within the URL query string. |
| repositoryID | repository ID | cl0e3lc0c002318m |
| severity | severity of writeup (Critical, High, Medium, Low and Informational) | Critical |
| description | description of writeup | The application responds to login submissions with a link containing the user's password within the URL query string. |
| recommendations | writeup recommendation | The application should never transmit any sensitive information within the URL query string. |
| references | writeup references | CVE-2017-0267 |
| fields | this is the parent parameter; each parent requires an additional parameter label and value | label: "Source"  <br>value: "website" |
| tags | any tags associated with the writeup, to be separated by a comma | pentest, enclave_99, crown_jewel |
| doc_type | writeup document type | template |
| tenantID | tenant ID that writeup exists under | 40632 |
| source | this identifies the source of the writeup | custom |
    """
    name = "Create Writeups"
    root = "/api/v1"
    path = f'/template/create'
    return request.post(base_url, headers, root+path, name, payload)

def update_writeups(base_url, headers, writeupId, payload):
    """
    This request **updates** an existing writeup for a tenant.

The `instanceUrl` is needed to execute the call.

Below is a list of information needed to fulfil the request.

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| title | writeup title | Password returned in URL query string |
| repositoryID | repository ID | cl0e3lc0c002318m |
| severity | severity of writeup | Critical |
| description | description of writeup | The application responds to login submissions with a link containing the user's password within the URL query string. |
| recommendations | writeup recommendation | The application should never transmit any sensitive information within the URL query string. |
| references | writeup references | CWE-598: Information Exposure Through Query Strings in GET Request |
| fields | this is the parent parameter; each parent requires an additional parameter label and value | label: "Source"  <br>value: "website" |
| doc_id | document ID | 104560 |
| doc_type | document type | template |
| source | writeup source | Custom |
| tenantId | tenant ID that writeup exists under | 40632 |
| id | template ID | template_104560 |
    """
    name = "Update Writeups"
    root = "/api/v1"
    path = f'/template/{writeupId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_writeups(base_url, headers, writeupId):
    """
    This request will **delete** a writeup from **WriteupsDB** by providing the instance url and writeup ID.

The `instanceUrl` is needed to execute the call.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| message | validation of delete request | success |
| doc_id | ID of writeup deleted | template_104560 |
    """
    name = "Delete Writeups"
    root = "/api/v1"
    path = f'/template/{writeupId}'
    return request.delete(base_url, headers, root+path, name)

def add_writeup_to_report(base_url, headers, writeupId, payload):
    """
    See v2 endpoint [Bulk Add Writeups to Report](https://api-docs.plextrac.com/#3806f48a-985b-4a63-b90f-9ca18e4a499b)

This request will **add a writeup** to a report.

**NOTE:** The finding created will have it's Date Reported set to the date the Writeup was added to PT, not the date this endpoint was called and the finding created in the report.
    """
    name = "Add Writeup to Report"
    root = "/api/v1"
    path = f'/copy/{writeupId}'
    return request.put(base_url, headers, root+path, name, payload)
