from utils import request_handler as request

def retreive_analytics_findings(base_url, headers, payload):
    """
    This request retrieves **analytics on findings and reports per client,** providing a total count of per client and total count by severity.
    """
    name = "Retreive Analytics Findings"
    root = "/api/v1"
    path = f'/clients/analytics/findings'
    return request.post(base_url, headers, root+path, name, payload)

def retreive_analytics_findings_aging(base_url, headers, payload):
    """
    This request retrieves **analytics on findings based on the date of finding** per client, providing a total count of findings per client and total count by severity. The query defaults to 30 days but can be set to 60 and 90 days.
    """
    name = "Retreive Analytics Findings Aging"
    root = "/api/v1"
    path = f'/clients/analytics/findings/aging'
    return request.post(base_url, headers, root+path, name, payload)

def get_analytics_bootstrap_findings(base_url, headers, payload):
    """
    This request retrieves **asset** **analytics on findings** per client.
    """
    name = "Get Analytics Bootstrap Findings"
    root = "/api/v1"
    path = f'/clients/analytics/bootstrap'
    return request.get(base_url, headers, root+path, name, payload)

def get_analytics_finding_aging(base_url, headers, clientId):
    """
    This request retrieves **analytics on findings based on the date of finding** per client, providing a total count of findings per client and total count by severity. The query defaults to 30 days but can be set to 60 and 90 days.

NOTE: The term "flaws" refers to findings.
    """
    name = "Get Analytics Finding Aging"
    root = "/api/v1"
    path = f'/client/{clientId}/analytics/flaws/aging'
    return request.get(base_url, headers, root+path, name)
