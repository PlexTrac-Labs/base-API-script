from utils import request_handler as request

def get_user_permissions(base_url, headers, tenantId, userId):
    """
    Gets a user's RBAC permissions.
    """
    name = "Get User Permissions"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/user/{userId}/permissions'
    return request.get(base_url, headers, root+path, name)

def get_role_users(base_url, headers, tenantId, roleKey):
    """
    Gets all users associated with a certain RBAC security role.
    """
    name = "Get Role Users"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleKey}/users'
    return request.get(base_url, headers, root+path, name)

def add_role_user(base_url, headers, tenantId, roleId, payload):
    """
    Adds a user to an RBAC Security Role.

**Important:** It is highly recommended to perform this action in the Plextrac platform. There is a permissions wizard that goes through multiple steps to make sure a user is assigned the correct permissions throughout the app.
    """
    name = "Add Role User"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}/users'
    return request.put(base_url, headers, root+path, name, payload)

def remove_role_user(base_url, headers, tenantId, roleId, userId):
    """
    Removes a user from an RBAC security role.
    """
    name = "Remove Role User"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/security/role/{roleId}/users/{userId}'
    return request.delete(base_url, headers, root+path, name)
