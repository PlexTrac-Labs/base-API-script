from utils import request_handler as request

def get_findings_by_report(base_url, headers, clientId, reportId, payload):
    """
    This request **retrieves a list of findings for a specific report.**
    """
    name = "Get Findings by Report"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/findings'
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

def bulk_update_findings(base_url, headers, clientId, reportId, payload):
    """
    get a paginated list of affected assets by finding id
    """
    name = "Bulk Update Findings"
    root = "/api/v2"
    path = f'/clients/{clientId}/reports/{reportId}/findings'
    return request.put(base_url, headers, root+path, name, payload)

def bulk_get_evidence(base_url, headers, tenantId, clientId, reportId, findingId, payload):
    """
    This request **retrieves evidence information** for a specific finding for a specific report.
    """
    name = "Bulk Get Evidence"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence'
    return request.post(base_url, headers, root+path, name, payload)

def update_evidence(base_url, headers, clientId, reportId, findingId, assetId, evidenceId, payload):
    """
    This request **updates evidence for a specific asset and finding**.
    """
    name = "Update Evidence"
    root = "/api/v2"
    path = f'/client/{clientId}/report/{reportId}/finding/{findingId}/asset/{assetId}/evidence/{evidenceId}'
    return request.put(base_url, headers, root+path, name, payload)

def bulk_upsert_evidence(base_url, headers, tenantId, clientId, reportId, findingId, payload):
    """
    This request **inserts evidence information in bulk** and creates new evidence without adding it to an affected asset.

The `id` should be an existing or new UUID
    """
    name = "Bulk Upsert Evidence"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/report/{reportId}/finding/{findingId}/asset/evidence'
    return request.put(base_url, headers, root+path, name, payload)

def copy_finding_to_writeups_repository(base_url, headers, payload):
    """
    This request **copies a finding from a report** and puts into a **WriteUpsDB** repository.
    """
    name = "Copy Finding to Writeups Repository"
    root = "/api/v2"
    path = f'/repositories/copyFlawToWriteupsRepository'
    return request.post(base_url, headers, root+path, name, payload)
