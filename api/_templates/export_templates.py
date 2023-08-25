from utils import request_handler as request

def list_export_templates(base_url, headers, tenantId):
    """
    Returns a list of all Export Templates in the tenant.
    """
    name = "List Export Templates"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/export-templates'
    return request.get(base_url, headers, root+path, name)
