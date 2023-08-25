from utils import request_handler as request

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
