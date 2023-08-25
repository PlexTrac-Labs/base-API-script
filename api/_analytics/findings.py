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

def get_finding_analytics_bootstrap(base_url, headers, payload):
    """
    StartFragment

This request retrieves **finding analytics** based on filters.

Payload params:

| **Parameter** | **Required (y/n)** | **Type** |
| --- | --- | --- |
| clients | y | array\[number\] |
| clientTags | y | array\[string\] |
| assetTags | y | array\[string\] |
| reports | y | array\[number\] |
| reportTags | y | array\[string\] |
| findingTags | y | array\[string\] |
| order | y | array\[string\] where valid strings are in the list: "reportTags", "clients", "reportTags", "findingTags", "reports", "assetTags", "assignees", "assetPorts", "operatingSystem", "dataOwner", "systemOwner", "physicalLocation", "cveIDs", "cweIDs" |
| assetPagination | n | see table below |
| runbooks | n | array\[string\] |
| methodologies | n | array\[string\] |
| engagements | n | array\[string\] |
| engagementTags | n | array\[string\] |
| tactics | n | array\[string\] |
| assignees | n | array\[string\] |
| assetPorts | n | array\[string\] |
| operatingSystem | n | array\[string\] |
| dataOwner | n | array\[string\] |
| systemOwner | n | array\[string\] |
| physicalLocation | n | array\[string\] |
| cveIDs | n | array\[string\] |
| cweIDs | n | array\[string\] |

EndFragment

  
assetPagination

| **Parameter** | **Required** | **Type** |
| --- | --- | --- |
| limit | y | number |
| offset | y | number |
| total | y | number |
| search | y | string: allows empty string |
    """
    name = "Get Finding Analytics Bootstrap"
    root = "/api/v2"
    path = f'/findingAnalytics/bootstrap'
    return request.post(base_url, headers, root+path, name, payload)
