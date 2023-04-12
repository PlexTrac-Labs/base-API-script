from utils import request_handler as request

def get_tenant_users(base_url, headers, tenantId):
    """
    This request **retrieves a list of all users** in a tenant.
    """
    name = "Get Tenant Users"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/users'
    return request.get(base_url, headers, root+path, name)
