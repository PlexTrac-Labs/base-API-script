from utils import request_handler as request

def get_integration(base_url, headers, tenantId, product):
    """
    No description in Postman
    """
    name = "Get Integration"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/integrations/{product}'
    return request.get(base_url, headers, root+path, name)

def save_integration(base_url, headers, tenantId, product, payload):
    """
    No description in Postman
    """
    name = "Save Integration"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/integrations/{product}'
    return request.post(base_url, headers, root+path, name, payload)

def delete_integration(base_url, headers, tenantId, product):
    """
    No description in Postman
    """
    name = "Delete Integration"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/integrations/{product}'
    return request.delete(base_url, headers, root+path, name)

def tenableio_get_tags(base_url, headers):
    """
    No description in Postman
    """
    name = "TenableIO Get Tags"
    root = "/api/v2"
    path = f'/integrations/tenable-io/tags'
    return request.get(base_url, headers, root+path, name)

def tenableio_sync_tags(base_url, headers):
    """
    No description in Postman
    """
    name = "TenableIO Sync Tags"
    root = "/api/v2"
    path = f'/integrations/tenable-io/tags/sync'
    return request.get(base_url, headers, root+path, name)
