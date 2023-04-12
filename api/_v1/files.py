from utils import request_handler as request

def download_an_artifact(base_url, headers):
    """
    No description in Postman
    """
    name = "Download an artifact"
    root = "/api/v1"
    path = f'/file-manager/artifacts/981a9b85-f086-491a-9ecc-89a821f8a475'
    return request.get(base_url, headers, root+path, name)

def upload_an_artifact_json(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Upload an artifact (json)"
    root = "/api/v1"
    path = f'/file-manager/upload'
    return request.post(base_url, headers, root+path, name, payload)

def upload_an_artifact_file(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Upload an artifact (file)"
    root = "/api/v1"
    path = f'/file-manager/upload'
    return request.post(base_url, headers, root+path, name, payload)

def get_artifacts(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Get artifacts"
    root = "/api/v1"
    path = f'/file-manager/artifacts'
    return request.post(base_url, headers, root+path, name, payload)

def delete_an_artifact(base_url, headers):
    """
    No description in Postman
    """
    name = "Delete an artifact"
    root = "/api/v1"
    path = f'/file-manager/artifacts/981a9b85-f086-491a-9ecc-89a821f8a475'
    return request.delete(base_url, headers, root+path, name)

def get_upload_by_name(base_url, headers):
    """
    No description in Postman
    """
    name = "Get Upload by Name"
    root = "/api/v1"
    path = f'/uploads/2d18530e-fa9c-4a4a-a494-b3e3bdb42007.jpg'
    return request.get(base_url, headers, root+path, name)

def upload_image_to_tenant(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Upload Image to Tenant"
    root = "/api/v1"
    path = f'/uploads'
    return request.post(base_url, headers, root+path, name, payload)
