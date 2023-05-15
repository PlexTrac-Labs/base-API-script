from utils import request_handler as request

def get_mailer_templates(base_url, headers, tenantId) -> PTWrapperLibraryResponse:
    """
    Get Mailer Templates
    """
    name = "Get Mailer Templates"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/mailer/templates'
    return request.get(base_url, headers, root+path, name)

def get_email_template(base_url, headers, tenantId) -> PTWrapperLibraryResponse:
    """
    Get Email Template
    """
    name = "Get Email Template"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD'
    return request.get(base_url, headers, root+path, name)

def upsert_email_template(base_url, headers, tenantId, payload) -> PTWrapperLibraryResponse:
    """
    Upsert Email Template
    """
    name = "Upsert Email Template"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/mailer/templates/FORGOTTEN_PASSWORD'
    return request.put(base_url, headers, root+path, name, payload)
