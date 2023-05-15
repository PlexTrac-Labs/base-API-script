from utils import request_handler as request

def list_clients(base_url, headers):
    """
    This request retrieves **all** clients for a tenant that you are **authorized** to view.

The `instanceUrl` is needed to execute the call.

A successful call returns a List of JSON objects with summarized information about each client.

Below is the structure of the summaried JSON returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| id | full client ID | client_1254 |
| doc_id | List with a single value of client ID | \[1254\] |
| data | List of information about hte client:  <br>client id  <br>client name  <br>null value | \[1254, "Karbo Industries", null\] |
    """
    name = "List Clients"
    root = "/api/v1"
    path = f'/client/list'
    return request.get(base_url, headers, root+path, name)

def get_client(base_url, headers, clientId):
    """
    This request retrieves information on a client for a tenant that you are **authorized** to view.

The `instanceUrl` and `clientId` is needed to execute the call.

A successsfull call returns the JSON object of the cient stored in hte DB. See [Client Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object) for deatils on how this JSON is structured
    """
    name = "Get Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.get(base_url, headers, root+path, name)

def create_client(base_url, headers, payload):
    """
    This request **creates** a new client within a tenant.

The `instanceUrl` is needed to execute the call.

In addition to the example below, see [Client Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object) for details on the payload structure

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| client_id | Id of the newly created client | 1234 |
| assign_message | dictionary that summarizes which users were granted acces to the client. This includes the user issuing the request and any user in the default group. |  |

`assign_message` dictionary structure

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | status of assigning users to new client | complete |
| users_assigned | List of user emails that were assigned to client | \["test@email.com"\] |
| users_rejected | List of user emails that failed to get assigned to client | \["test@email.com"\] |
    """
    name = "Create Client"
    root = "/api/v1"
    path = f'/client/create'
    return request.post(base_url, headers, root+path, name, payload)

def update_client(base_url, headers, clientId, payload):
    """
    This request updates an existing client within a tenant.

The `instanceUrl` and `clientId` is needed to execute the call.

In addition to the example below, see [Client Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/client-object) for details on the payload structure.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | explanation of request | Client updated successfully. |
    """
    name = "Update Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_client(base_url, headers, clientId):
    """
    This request **removes** a client from a tenant.

The `instanceUrl` and `clientId` is needed to execute the call.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of delete request | success |
| message | explanation of request | client deleted successfully |
    """
    name = "Delete Client"
    root = "/api/v1"
    path = f'/client/{clientId}'
    return request.delete(base_url, headers, root+path, name)

def add_client_logo(base_url, headers, clientId, payload):
    """
    This request **creates** a logo for a client. The file must be JPEG or PNG.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | further validation | Client Logo Updated |
    """
    name = "Add Client Logo"
    root = "/api/v1"
    path = f'/client/{clientId}/logo'
    return request.post(base_url, headers, root+path, name, payload)

def delete_client_logo(base_url, headers, clientId, payload):
    """
    This request **removes** a logo for a client.

The `instanceUrl` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of request | success |
| message | further validation | Client Logo Updated |
    """
    name = "Delete Client Logo"
    root = "/api/v1"
    path = f'/client/{clientId}/logo'
    return request.delete(base_url, headers, root+path, name, payload)

def list_tenant_client_users(base_url, headers, tenantId, clientId):
    """
    This request **retrieves a list of all users** for a specific client.
    """
    name = "List Tenant Client Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users'
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

def remove_user_from_client(base_url, headers, tenantId, clientId, payload):
    """
    Revoke a user's authorization from a client
    """
    name = "Remove User from Client"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/user/remove'
    return request.post(base_url, headers, root+path, name, payload)

def available_tenant_users(base_url, headers, tenantId, clientId):
    """
    No description in Postman
    """
    name = "Available Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/users/available'
    return request.get(base_url, headers, root+path, name)
