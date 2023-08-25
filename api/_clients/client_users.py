from utils import request_handler as request

def list_client_users_v1(base_url, headers, tenantId, clientId):
    """
    This request **retrieves a list of all users** for a specific client.
    """
    name = "List Client Users v1"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users'
    return request.get(base_url, headers, root+path, name)

def list_client_users_v2(base_url, headers, tenantId, clientId):
    """
    This request retrieves a list of **all** **users** for a specific client.
    """
    name = "List Client Users v2"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/users'
    return request.get(base_url, headers, root+path, name)

def available_tenant_users(base_url, headers, tenantId, clientId):
    """
    No description in Postman
    """
    name = "Available Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users/available'
    return request.get(base_url, headers, root+path, name)

def assign_user_to_client(base_url, headers, tenantId, clientId, payload):
    """
    DEPRECATED - See v2 [Bulk Assign Users to Client](https://api-docs.plextrac.com/#8b017c78-cdcf-4046-9d25-ca6d0dcb1d82)

Known Bug

Will not honor the `role` or `classificationId` entered. Will instead set the client permission level the same as the users default level.

Assign a user to a client within your tenancy
    """
    name = "Assign User to Client"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/user/assign'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_assign_users_to_client(base_url, headers, tenantId, clientId, payload):
    """
    This request **assigns a list of users to have a certain level of permission for a specific client**.

The role is the level of access a user will be assigned for the client being added to. This can differ from the default role a user is assigned.

For example: A user can have the _Analyst_ role assigned as the default role that will be apply to all clients they have access to. They can then be assigned the _Standard User_ role for a certain client, adding thee extra permissions when inside that specific client.

The "role" field must contain the RBAC role code. The codes for the default roles are:

Administrator - `ADMIN`

Standard User - `STD_USER`

Analyst - `ANALYST`

A custom RBAC role will have a role code created in the format

Custom Role - `TENANT_0_ROLE_CUSTOM_ROLE`

The rest of the fields should match the values of the existing user.
    """
    name = "Bulk Assign Users to Client"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/bulk/users/assign'
    return request.post(base_url, headers, root+path, name, payload)

def remove_user_from_client(base_url, headers, tenantId, clientId, payload):
    """
    Revoke a user's authorization from a client
    """
    name = "Remove User from Client"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/user/remove'
    return request.post(base_url, headers, root+path, name, payload)
