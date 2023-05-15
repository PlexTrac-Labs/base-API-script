from utils import request_handler as request

def get_artifacts(base_url, headers, payload):
    """
    Return a list of filtered artifact files.

The `components` property is optional.
    """
    name = "Get artifacts"
    root = "/api/v1"
    path = f'/file-manager/artifacts'
    return request.post(base_url, headers, root+path, name, payload)

def download_an_artifact(base_url, headers, artifactId):
    """
    No description in Postman
    """
    name = "Download an artifact"
    root = "/api/v1"
    path = f'/file-manager/artifacts/{artifactId}'
    return request.get(base_url, headers, root+path, name)

def upload_an_artifact_file(base_url, headers, payload):
    """
    Uploads a file to the tenant. These files live in a single location and are related to clients and reports through the `relations` attribute. Each file has a list of `components` or categorys it belongs to. This is used for filtering when loading files to display in platform. Files with different components are displayed in different locations.

**Components used in platform:**

report_artifacts

**Relation models used in platform:**

{"model":"client","id":"1234"}

{"model":"report","id":"123456"}

{"model":"assessment_question","id":"clc0syuip005a0zo3cv3p87ic"}

**Accepted file MIME types:**

'application/x-python-code',  
'applicaiton/x-python',  
'application/json',  
'application/pdf',  
'application/xml',  
'application/msword',  
'application/octet-stream',  
'application/vnd.openxmlformats-officedocument.wordprocessingml.document',  
'application/vnd.ms-excel',  
'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',  
'application/vnd.oasis.opendocument.text',  
'application/x-zip-compressed',  
'application/vnd.oasis.opendocument.spreadsheet',  
'application/zip',  
'application/x-7z-compressed',  
'image/bmp',  
'image/gif',  
'image/jpeg',  
'image/png',  
'text/plain',  
'text/html',  
'text/xml',  
'text/x-python',  
'text/x-python-script',  
'text/x-sh',  
'text/javascript',  
'text/csv',  
'video/mp4',  
'video/quicktime',  
'video/mpeg',  
'video/x-msvideo',  
'video/x-ms-wmv'
    """
    name = "Upload an artifact (file)"
    root = "/api/v1"
    path = f'/file-manager/upload'
    return request.post(base_url, headers, root+path, name, payload)

def delete_an_artifact(base_url, headers, artifactId):
    """
    This request **deletes an artifact** from the tenant.

Will return a 404 error if an artifact is not found with the provided `artifactId`.
    """
    name = "Delete an artifact"
    root = "/api/v1"
    path = f'/file-manager/artifacts/{artifactId}'
    return request.delete(base_url, headers, root+path, name)
