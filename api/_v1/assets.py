from utils import request_handler as request

def get_asset_list(base_url, headers, clientId):
    """
    This request **retrieves a list of all assets** for a specific client.
    """
    name = "Get Asset List"
    root = "/api/v1"
    path = f'/client/{clientId}/assets'
    return request.get(base_url, headers, root+path, name)

def get_asset(base_url, headers, clientId, assetId):
    """
    This request **retrieves a specific asset** for a specific client.
    """
    name = "Get Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/{assetId}'
    return request.get(base_url, headers, root+path, name)

def create_asset(base_url, headers, clientId, payload):
    """
    This request **creates an asset** for a client. Currently an endpoint for creating an asset does not exist, so use this endpoint with an ID value of "0" to have a new unique asset ID created.
    """
    name = "Create Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/0'
    return request.put(base_url, headers, root+path, name, payload)

def update_asset(base_url, headers, clientId, assetId, payload):
    """
    This request **updates a specific asset** for a client.
    """
    name = "Update Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/{assetId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_asset(base_url, headers, clientId, assetId):
    """
    This request **deletes a specific asset** for a client.
    """
    name = "Delete Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/{assetId}'
    return request.delete(base_url, headers, root+path, name)

def import_client_assets(base_url, headers, clientId, source, payload):
    """
    Deprecated. Please use [https://api-docs.plextrac.com/#f77e7699-7ccb-4d80-b74b-d516350ee8cc](https://api-docs.plextrac.com/#f77e7699-7ccb-4d80-b74b-d516350ee8cc)
    """
    name = "Import Client Assets"
    root = "/api/v1"
    path = f'/client/{clientId}/assets/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_delete_client_assets(base_url, headers, clientId, payload):
    """
    This requests deletes the Client Assets sent in the payload.

IMPORTANT: This will not unlink and finding that are currently affecting the assets to be deleted. Before calling this endpoint you must use the [DELETE Remove Affected Asset from Flaw](https://api-docs.plextrac.com/#45198986-d6c2-45a9-8411-cbafab565d0e) endpoint to unlink all findings affecting the assets to be deleted.
    """
    name = "Bulk Delete Client Assets"
    root = "/api/v1"
    path = f'/client/{clientId}/bulk/assets/delete'
    return request.post(base_url, headers, root+path, name, payload)

def remove_affected_asset_from_flaw(base_url, headers, clientId, reportId, findingId, assetId):
    """
    No description in Postman
    """
    name = "Remove Affected Asset from Flaw"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}'
    return request.delete(base_url, headers, root+path, name)

def get_scanner_output(base_url, headers, clientId, reportId, findingId, assetId):
    """
    No description in Postman
    """
    name = "Get Scanner Output"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/scanoutput'
    return request.get(base_url, headers, root+path, name)

def get_affected_asset_status_list(base_url, headers, clientId, reportId, findingId, assetId):
    """
    No description in Postman
    """
    name = "Get Affected Asset Status List"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status'
    return request.get(base_url, headers, root+path, name)

def create_affected_asset_status(base_url, headers, clientId, reportId, findingId, assetId):
    """
    No description in Postman
    """
    name = "Create Affected Asset Status"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}/status/update'
    return request.post(base_url, headers, root+path, name)
