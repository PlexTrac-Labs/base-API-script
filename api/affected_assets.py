from utils import request_handler as request

def import_finding_affected_assets(base_url, headers, clientId, reportId, findingId, source, payload):
    """
    URL **source** accepts 'csv', 'xml'

File size limit 1gb file
    """
    name = "Import Finding Affected Assets"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected-assets/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def get_affected_assets_by_finding(base_url, headers, clientId, reportId, findingId, offset, limit, order, filter, status):
    """
    Deprecated. Please use [Get Finding](https://api-docs.plextrac.com/#2744f99d-bf3a-4174-93f6-a0f05e99fcdc)

This request **retrieves a paginated list of assets** for a specific finding in a specific report.

    Query Parameters:
    offset: (number, default: 0) pagination offset - example (0)
    limit: (number, default: 10) pagination limit - example (10)
    order: (string, default: ascend) order by asset name ascend/descend - example (ascend)
    filter: (string) filter by asset name - example ()
    status: (string) Open/Closed/In Process, filter by asset status - example ()
    """
    name = "Get Affected Assets by Finding"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/flaws/{findingId}/affected_assets?offset={offset}?limit={limit}?order={order}?filter={filter}?status={status}'
    return request.get(base_url, headers, root+path, name)

def remove_affected_asset_from_flaw(base_url, headers, clientId, reportId, findingId, assetId):
    """
    No description in Postman
    """
    name = "Remove Affected Asset from Flaw"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/asset/{assetId}'
    return request.delete(base_url, headers, root+path, name)

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
