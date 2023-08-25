from utils import request_handler as request

def list_report_findings(base_url, headers, clientId, reportId):
    """
    This request **retrieves a list of findings for a specific report**.
    """
    name = "List Report Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaws'
    return request.get(base_url, headers, root+path, name)

def get_findings_by_report(base_url, headers, clientId, reportId, payload):
    """
    This request **retrieves a list of findings for a specific report.**

**pagination.limit** options:

1, 10, 50, 100, 99999
    """
    name = "Get Findings by Report"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/findings'
    return request.post(base_url, headers, root+path, name, payload)

def get_finding(base_url, headers, clientId, reportId, findingId):
    """
    This request **retrieves a specific finding** from a report.

See our docs on the [Finding Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object) structure for more details on the response.
    """
    name = "Get Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.get(base_url, headers, root+path, name)

def create_finding(base_url, headers, clientId, reportId, payload):
    """
    This request **creates a finding** for a specific report.

See our docs on the [Finding Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object) structure for more details on possible keys.

**Affected Assets**

A finding's `affected_assets` are a copy of a `client_asset` with additional affected fields. When **adding a new** asset to a finding's affected_assets, you should use the [GET Get Asset](https://api-docs.plextrac.com/#5fa9e7be-55d3-452e-8562-00ba4a137782) endpoint, then add the following keys. See our docs on the [Asset Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/asset-object) structure for more details about these affected fields.

- ports
- status
- locationUrl
- vulnerableParameters
- evidence
- notes
    

Then add this modified asset object to the finding's `affected_assets` dictionary with the key being a string of the asset's `id` and the value being the modified asset object.

**Registering Tags**

When a finding is created in the UI there are a few processes that get kicked off that do not happen when calling this endpoint directly.

Any tags added to the finding that have not been added anywhere else in the instnace will be added to the finding but NOT to the list of tenant tags. This means when you start typing to add a tag anywhere in the platform, the dropdown list that pops up will not have the new tags since they weren't added to the listed of tenant tags.
    """
    name = "Create Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/create'
    return request.post(base_url, headers, root+path, name, payload)

def update_finding(base_url, headers, clientId, reportId, findingId, payload):
    """
    This request **updates a specific finding** for a specific report.

See our docs on the [Finding Object](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api/object-structures/finding-object) structure for more details on possible keys.

**Note:**

This PUT request is meant to **replace** the finding object in the DB. Use the [GET Get Finding](https://api-docs.plextrac.com/#e903c288-8807-4df9-962f-0d86f76d9df8) endpoint to get the current finding, make necessary changes, then send that object in the payload to update the finding.

The example payloads shown here do not have all the possible properties on a finding, but only acts as an example. Each finding will be slightly different depending on what data is on the finding. Some property keys won't be added to a finding until that data is added to the finding.

**Affected Assets**

A finding's `affected_assets` are a copy of a `client_asset` with additional affected fields. When **adding a new** asset to a finding's affected_assets, you should use the GET Get Asset endpoint, then add the following keys:

- ports
- status
- locationUrl
- vulnerableParameters
- evidence
- notes
    

Then add this modified asset object to the finding's `affected_assets` dictionary with the key being a string of the asset's `id` and the value being the modified asset object.
    """
    name = "Update Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.put(base_url, headers, root+path, name, payload)

def bulk_update_findings(base_url, headers, clientId, reportId, payload):
    """
    get a paginated list of affected assets by finding id
    """
    name = "Bulk Update Findings"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/findings'
    return request.put(base_url, headers, root+path, name, payload)

def delete_finding(base_url, headers, clientId, reportId, findingId):
    """
    This request **deletes a specific finding** from a specific report.
    """
    name = "Delete Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.delete(base_url, headers, root+path, name)

def bulk_delete_findings(base_url, headers, clientId, reportId, payload):
    """
    This request **enables a bulk deletion of findings** from a report.
    """
    name = "Bulk Delete Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaws/delete'
    return request.post(base_url, headers, root+path, name, payload)

def get_finding_status_list(base_url, headers, clientId, reportId, findingId):
    """
    This request **retrieves the status of a specific finding** from a report.
    """
    name = "Get Finding Status List"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/status'
    return request.get(base_url, headers, root+path, name)

def create_status_update(base_url, headers, clientId, reportId, findingId, payload):
    """
    This request **updates the status of a specific finding** from a report.

Note: The request should include the entire `findings` object, which is documented in the `update` and `post` methods of this section.
    """
    name = "Create Status Update"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/status/update'
    return request.post(base_url, headers, root+path, name, payload)

def get_affected_assets_by_finding(base_url, headers, clientId, reportId, findingId, offset, limit, order, filter, status):
    """
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
