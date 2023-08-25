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
| risk_score | used for CVSS 3.1 scores (other CVSS version are handled in \`fields\`) |  |
| calculated_severity | boolean of whether the finding severity was set by the calculated CVSS3.1 score | true |
| common_identifiers | CVE and CWE data |  |
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
| risk_score | used for CVSS 3.1 scores (other CVSS version are handled in \`fields\`) |  |
| calculated_severity | boolean of whether the finding severity was set by the calculated CVSS3.1 score | true |
| common_identifiers | CVE and CWE data |  |
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

def bulk_add_writeups_to_report(base_url, headers, payload):
    """
    This request adds **a writeup** in the **WriteupsDB** module to an existing report.
    """
    name = "Bulk Add Writeups to Report"
    root = "/api/v2"
    path = f'/writeups/bulk/addToReport'
    return request.post(base_url, headers, root+path, name, payload)

def copy_finding_to_writeups_repository(base_url, headers, payload):
    """
    **Deprecated**: Since this endpoint's payload requires the finding object, it proves the same functionality as [POST Copy Finding to Writeups Repository](https://api-docs.plextrac.com/#e05be880-df62-4eca-8b5f-cc98b7ce7e2a) which should be used instead.

This request **copies a finding from a report** and puts into a **WriteUpsDB** repository.
    """
    name = "Copy Finding to Writeups Repository"
    root = "/api/v2"
    path = f'/repositories/copyFlawToWriteupsRepository'
    return request.post(base_url, headers, root+path, name, payload)

def get_writeups_from_repository(base_url, headers, repositoryId, payload):
    """
    This request **retrieves all writeups from a specific repository** in the **WriteupsD**B module.
    """
    name = "Get Writeups from Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/getWriteups'
    return request.post(base_url, headers, root+path, name, payload)

def add_writeups_to_repository(base_url, headers, repositoryId, payload):
    """
    This request **moves a writeup** in the **WriteupsDB** module to different repository.
    """
    name = "Add Writeups to Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/addWriteups'
    return request.post(base_url, headers, root+path, name, payload)

def import_writeups_to_repository(base_url, headers, source, payload):
    """
    This request **imports a csv of writeups** to the **WriteupsDB** module.

In the URL the source should be `csv`.
    """
    name = "Import Writeups to Repository"
    root = "/api/v2"
    path = f'/writeups/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def remove_writeups_from_repository(base_url, headers, repositoryId, payload):
    """
    This request removes **a writeup from a specific repository** in the **WriteupsDB** module.
    """
    name = "Remove Writeups from Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/removeWriteup'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_copy_writeups(base_url, headers, payload):
    """
    This request **copies writeups from a repository** in the **WriteupsDB** module.
    """
    name = "Bulk Copy Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/copy'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_move_writeups(base_url, headers, payload):
    """
    This request **moves a writeup to another repository** in the **WriteupsDB** module.
    """
    name = "Bulk Move Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/move'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_delete_writeups(base_url, headers, payload):
    """
    This request **deletes a writeup** in the **WriteupsDB** module.
    """
    name = "Bulk Delete Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/delete'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_add_tags_to_writeups(base_url, headers, payload):
    """
    This request **adds tags to a writeup** in the **WriteupsDB** module.
    """
    name = "Bulk Add Tags to Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/tags'
    return request.post(base_url, headers, root+path, name, payload)
