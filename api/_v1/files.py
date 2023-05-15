from utils import request_handler as request

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
