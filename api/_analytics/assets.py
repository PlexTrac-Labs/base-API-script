from utils import request_handler as request

def retrieve_analytics_assets(base_url, headers, payload):
    """
    This request **retrieves information about assets** stored in the **Clients** module.

POST:

*   clients: int\[\]
*   type: string\[\]
*   criticality: string\[\]
*   data_owner: string
*   physical_location: string
*   system_owner: string
*   tags: { assets: string\[\] }
    """
    name = "Retrieve Analytics Assets"
    root = "/api/v2"
    path = f'/clients/analytics/assets/overview'
    return request.post(base_url, headers, root+path, name, payload)

def retrieve_analytics_assets_with_filter(base_url, headers, payload, limit, offset):
    """
    This request **retrieves information about assets** stored under clients and provides the ability to filter and limit the data set returned.

POST:

*   clients: int\[\]
*   type: string\[\]
*   criticality: string\[\]
*   data_owner: string
*   physical_location: string
*   system_owner: string
*   tags: { assets: string\[\] }
    

GET:

*   limit: int (default 10)
*   offset: int (default 0)

    Query Parameters:
    limit: No description in Postman - example (10)
    offset: No description in Postman - example (0)
    """
    name = "Retrieve Analytics Assets with Filter"
    root = "/api/v2"
    path = f'/clients/analytics/assets?limit={limit}?offset={offset}'
    return request.post(base_url, headers, root+path, name, payload)
