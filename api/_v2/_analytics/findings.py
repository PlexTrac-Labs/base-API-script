from utils import request_handler as request

def get_finding_analytics_bootstrap(base_url, headers, payload) -> PTWrapperLibraryResponse:
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
