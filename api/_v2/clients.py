from utils import request_handler as request

def list_clients(base_url, headers, payload):
    """
    This request retrieves a list of **all** **clients** within a tenant. The body contains information on how to filter and sort the data to return.

{  
pagination: { // required object with keys "offset" & "limit"  
offset: 0, // required number, default 0  
limit: 25, // required number valid \[5, 25, 50, 100\]  
},  
sort: \[ // optional array of objects with keys "by" & "order"  
{  
by: "asset", // required string  
order: "DESC", // required one of "ASC" | "DESC"  
},  
\],  
filters: \[ // optional array of object with keys "by" & "value"  
{  
by: "asset", // required string  
value: "ba", // required string allows "empty string" if filtering by "tags" must be array of strings  
},  
\],  
}
    """
    name = "List Clients"
    root = "/api/v2"
    path = f'/clients'
    return request.post(base_url, headers, root+path, name, payload)

def list_client_users(base_url, headers, tenantId, clientId):
    """
    This request retrieves a list of **all** **users** for a specific client.
    """
    name = "List Client Users"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/users'
    return request.get(base_url, headers, root+path, name)

def list_client_findings(base_url, headers, clientId, payload):
    """
    This request retrieves **all findings** for **a specific client**. The specific finding info returned is a truncated version of the full finding info. Sorting and filters can be added to the request body.
    """
    name = "List Client Findings"
    root = "/api/v2"
    path = f'/client/{clientId}/findings'
    return request.post(base_url, headers, root+path, name, payload)

def list_client_assets(base_url, headers, clientId, payload):
    """
    This request retrieves **assets associated with a specific client**.
    """
    name = "List Client Assets"
    root = "/api/v2"
    path = f'/clients/{clientId}/assets'
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
