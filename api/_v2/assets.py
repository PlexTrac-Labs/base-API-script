from utils import request_handler as request

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

def import_client_assets(base_url, headers, clientId, source, payload):
    """
    This request imports assets from an outside tool into PlexTrac for a specific client.

The source must be from the supported list below:

*   nmap
*   csv
    

Includes support for a csv. Must use the schema described here:

[https://plextrac.atlassian.net/servicedesk/customer/portal/4/article/2116222984?src=-1968324237](https://plextrac.atlassian.net/servicedesk/customer/portal/4/article/2116222984?src=-1968324237)

When importing a csv file, the endpoint response contains the field `result`, which is the list of newly created asset ID strings. This list is the same order as the assets in the csv file that was used in the request.
    """
    name = "Import Client Assets"
    root = "/api/v2"
    path = f'/client/{clientId}/assets/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def list_report_assets(base_url, headers, reportId):
    """
    This request **retrieves a list of assets for a specific report.**
    """
    name = "List Report Assets"
    root = "/api/{{clientId}}"
    path = f'/reports/{reportId}/assets'
    return request.get(base_url, headers, root+path, name)

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
