from utils import request_handler as request

def list_tenant_clients(base_url, headers, tenantId):
    """
    List all clients of a given tenant
    """
    name = "List Tenant Clients"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/list'
    return request.get(base_url, headers, root+path, name)

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

def list_client_findings(base_url, headers, clientId, payload):
    """
    This request retrieves **all findings** for **a specific client**. The specific finding info returned is a truncated version of the full finding info. Sorting and filters can be added to the request body.

**filters.by**

| **`by`** **Key** | **`value`** **Data Type** |
| --- | --- |
| searchTerm | string |
| status | string |
| severity | string |
| reportId | integer |
| subStatus | string |
| visibility | string ("draft", or "published") |
| tags | array of strings |
| commonIdentifiers | array of strings representing CWE or CVE name i.e. \["CWE-998", "CVE-2022-44268"\] |
| dateFrom | integer - milliseconds from epoch |
| dateTo | integer - milliseconds from epoch |
| assignedTo | string |
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
