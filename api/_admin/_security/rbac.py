from utils import request_handler as request

def get_available_security_roles(base_url, headers, tenantId):
    """
    Gets a list of RBAC security roles and returns the `name` and `CUID` of each role.
    """
    name = "Get Available Security Roles"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/available'
    return request.get(base_url, headers, root+path, name)

def get_security_roles(base_url, headers, tenantId):
    """
    Get a list of RBAC security roles.
    """
    name = "Get Security Roles"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role'
    return request.get(base_url, headers, root+path, name)

def get_security_role(base_url, headers, tenantId, roleId):
    """
    Gets an RBAC security role.
    """
    name = "Get Security Role"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}'
    return request.get(base_url, headers, root+path, name)

def get_role_name_availability(base_url, headers, tenantId, payload):
    """
    Determines availability for a new RBAC Security Role.

The key value should have the format `TENANT_0_ROLE_[NAME_TO_CHECK]`

This is checking against a key generated from the name where letters are capital and spaces are replaced with underscores.
    """
    name = "Get Role Name Availability"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/availability'
    return request.post(base_url, headers, root+path, name, payload)

def create_security_role(base_url, headers, tenantId):
    """
    Creates a new RBAC security role.
    """
    name = "Create Security Role"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role'
    return request.post(base_url, headers, root+path, name)

def update_security_role_info(base_url, headers, tenantId, roleId, payload):
    """
    Updates a security role's info fields.
    """
    name = "Update Security Role Info"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}/info'
    return request.put(base_url, headers, root+path, name, payload)

def update_security_role_permission(base_url, headers, tenantId, roleId):
    """
    No description in Postman
    """
    name = "Update Security Role Permission"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}/permissions'
    return request.put(base_url, headers, root+path, name)

def delete_security_role(base_url, headers, tenantId, roleId):
    """
    No description in Postman
    """
    name = "Delete Security Role"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}'
    return request.delete(base_url, headers, root+path, name)
