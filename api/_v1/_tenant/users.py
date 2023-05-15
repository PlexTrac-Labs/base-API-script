from utils import request_handler as request

def list_tenant_users(base_url, headers, tenantId):
    """
    This request **retrieves a list of all users** in a tenant.
    """
    name = "List Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/list'
    return request.get(base_url, headers, root+path, name)

def create_user(base_url, headers, tenantId, payload):
    """
    Create a new user in your tenant
    """
    name = "Create User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create/bulk'
    return request.post(base_url, headers, root+path, name, payload)

def create_user_deprecated(base_url, headers, tenantId, payload):
    """
    Create a new user in your tenant

**This route is deprecated and will be blocked in a future release, please now call:{domain}/tenant/{tenantId}/user/create/bulk**
    """
    name = "Create User (DEPRECATED)"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create'
    return request.post(base_url, headers, root+path, name, payload)

def enabledisable_user(base_url, headers, tenantId, payload):
    """
    Toggle a user's authorization to your tenancy
    """
    name = "Enable/Disable User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/toggledisable'
    return request.post(base_url, headers, root+path, name, payload)
