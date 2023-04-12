from utils import request_handler as request

def get_findings_filtration(base_url, headers, clients, reports, date_from, date_to):
    """
    This request **retrieves a specific report** from a client with date filters.

    Query Parameters:
    clients: Array of client IDs - example ({{clientId}})
    reports: Array of Report IDs - example ({{reportId}})
    date_from: No description in Postman - example (2022-01-01)
    date_to: No description in Postman - example (2022-06-01)
    """
    name = "Get Findings (Filtration)"
    root = "/api/v1"
    path = f'/clients/findings?clients={clients}?reports={reports}?date_from={date_from}?date_to={date_to}'
    return request.get(base_url, headers, root+path, name)

def list_report_findings(base_url, headers, clientId, reportId):
    """
    This request **retrieves a list of findings for a specific report**.
    """
    name = "List Report Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaws'
    return request.get(base_url, headers, root+path, name)

def get_finding(base_url, headers, clientId, reportId, findingId):
    """
    This request **retrieves a specific finding** from a report.
    """
    name = "Get Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.get(base_url, headers, root+path, name)

def create_finding(base_url, headers, clientId, reportId, payload):
    """
    This request **creates a finding** for a specific report.
    """
    name = "Create Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/create'
    return request.post(base_url, headers, root+path, name, payload)

def update_finding(base_url, headers, clientId, reportId, findingId, payload):
    """
    This request **updates a specific finding** for a specific report.
    """
    name = "Update Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_finding(base_url, headers, clientId, reportId, findingId):
    """
    This request **deletes a specific finding** from a specific report.
    """
    name = "Delete Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}'
    return request.delete(base_url, headers, root+path, name)

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

def bulk_delete_findings(base_url, headers, clientId, reportId, payload):
    """
    This request **enables a bulk deletion of findings** from a report.
    """
    name = "Bulk Delete Findings"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaws/delete'
    return request.post(base_url, headers, root+path, name, payload)
