from utils import request_handler as request

def get_tenant_assets(base_url, headers, payload):
    """
    This request **retrieves the list of assets for a tenant**.

`pagination` is a required key while `sort` and `filters` are optional.

The `pagination.limit` must be one of \[5, 10, 25, 50, 100, 1000\]. The `pagination.offset` is the number of records to shift by, not the number of pages to shift by. i.e. offset 2, limit 10 gives you records 2-12 not 20-30

The following values can be used in the `sort.by` and `filters.by` field:

- searchTerm
- client_id
- assetCriticality
- tags
- type
- pci_status
- system_owner
- data_owner
    

The following values can be used in the `sort.order` field:

- ASC
- DESC
    """
    name = "Get Tenant Assets"
    root = "/api/v2"
    path = f'/tenant/assets'
    return request.post(base_url, headers, root+path, name, payload)

def get_assets_by_client(base_url, headers, clientId, payload):
    """
    This request **retrieves the list of assets for a specific client**.

`pagination` is a required key while `sort` and `filters` are optional.

The `pagination.limit` must be one of \[5, 10, 25, 50, 100\]. The `pagination.offset` is the number of records to shift by, not the number of pages to shift by. i.e. offset 2, limit 10 gives you records 2-12 not 20-30

The following values can be used in the `sort.by` and `filters.by` field:

- asset
- tags
    

The following values can be used in the `sort.order` field:

- ASC
- DESC
    

**Note**: To filter by assets without any tags, use the filter obj

{ "by": "tags", "value": \["none"\] }
    """
    name = "Get Assets by Client"
    root = "/api/v2"
    path = f'/clients/{clientId}/assets'
    return request.post(base_url, headers, root+path, name, payload)

def list_client_assets(base_url, headers, clientId):
    """
    This request **retrieves a list of all assets** for a specific client.
    """
    name = "List Client Assets"
    root = "/api/v1"
    path = f'/client/{clientId}/assets'
    return request.get(base_url, headers, root+path, name)

def list_report_assets(base_url, headers, reportId):
    """
    This request **retrieves a list of assets for a specific report.**
    """
    name = "List Report Assets"
    root = "/api/{{clientId}}"
    path = f'/reports/{reportId}/assets'
    return request.get(base_url, headers, root+path, name)

def get_asset(base_url, headers, clientId, assetId):
    """
    This request **retrieves a specific asset** for a specific client.

See our docs on the [Asset Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object) structure for more details on the response.
    """
    name = "Get Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/{assetId}'
    return request.get(base_url, headers, root+path, name)

def create_asset(base_url, headers, clientId, payload):
    """
    This request **creates an asset** for a client.

StartFragmentEndFragment

Currently an endpoint for creating an asset does not exist, use this endpoint with an ID value of "0" to have a new unique asset ID created.

See our docs on the [Asset Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object) structure for more details on possible keys.
    """
    name = "Create Asset"
    root = "/api/v1"
    path = f'/client/{clientId}/asset/0'
    return request.put(base_url, headers, root+path, name, payload)

def update_asset(base_url, headers, clientId, assetId, payload):
    """
    This request **updates a specific asset** for a client.

See ou rdocs on the [Asset Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object) structure for more details on possible keys.
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

def import_client_assets_v1(base_url, headers, clientId, source, payload):
    """
    Deprecated. Please use [https://api-docs.plextrac.com/#f77e7699-7ccb-4d80-b74b-d516350ee8cc](https://api-docs.plextrac.com/#f77e7699-7ccb-4d80-b74b-d516350ee8cc)
    """
    name = "Import Client Assets v1"
    root = "/api/v1"
    path = f'/client/{clientId}/assets/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def import_client_assets_v2(base_url, headers, clientId, source, payload, includeFullAssets):
    """
    This request imports assets from an outside tool into PlexTrac for a specific client.

The source must be from the supported list below:

- nmap
- csv
    

Includes support for a csv. Must use the schema described here:

[https://docs.plextrac.com/plextrac-documentation/product-documentation/clients/adding-assets-in-clients](https://docs.plextrac.com/plextrac-documentation/product-documentation/clients/adding-assets-in-clients)

When importing a csv file, the endpoint response contains the field `result`, which is the list of newly created asset ID strings. This list is the same order as the assets in the csv file that was used in the request.

    Query Parameters:
    includeFullAssets: Optional - This param determines whether the `result` list contains the asset IDs or the full asset object. - example (true)
    """
    name = "Import Client Assets v2"
    root = "/api/v2"
    path = f'/client/{clientId}/assets/import/{source}?includeFullAssets={includeFullAssets}'
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
