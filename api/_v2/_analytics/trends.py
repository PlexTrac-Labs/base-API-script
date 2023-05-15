from utils import request_handler as request

def analytics___trends___opened_closed(base_url, headers, payload):
    """
    POST:
- clients: int[]
- reports: int[]
- severity: string[]
- tags: { findings: string[], reports: string[] }
    """
    name = "Analytics - Trends - Opened Closed"
    root = "/api/v2"
    path = f'/clients/analytics/trends/opened-closed'
    return request.post(base_url, headers, root+path, name, payload)

def analytics___trends___from_creation_to_close(base_url, headers, payload):
    """
    POST:
- clients: int[]
- reports: int[]
- severity: string[]
- tags: { findings: string[], reports: string[] }
    """
    name = "Analytics - Trends - From creation to close"
    root = "/api/v2"
    path = f'/clients/analytics/trends/from-creation-to-close'
    return request.post(base_url, headers, root+path, name, payload)

def analytics___trends___age_of_open_findings(base_url, headers, payload):
    """
    POST:
- clients: int[]
- reports: int[]
- severity: string[]
- tags: { findings: string[], reports: string[] }
    """
    name = "Analytics - Trends - Age of open findings"
    root = "/api/v2"
    path = f'/clients/analytics/trends/age-of-open-findings'
    return request.post(base_url, headers, root+path, name, payload)

def analytics___trends___slas(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Analytics - Trends - SLAs"
    root = "/api/v2"
    path = f'/sla/analytics/mean-time'
    return request.post(base_url, headers, root+path, name, payload)

def analytics___trends___sla_findings(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Analytics - Trends - SLA Findings"
    root = "/api/v2"
    path = f'/sla/analytics/findings'
    return request.post(base_url, headers, root+path, name, payload)
