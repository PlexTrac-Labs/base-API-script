from utils import request_handler as request

def search__replace_in_report_occurrences(base_url, headers, payload):
    """
    This request **retrieves a count** of the number of occurrences that exist in a report for a given query. This will not result in any changes of data but only return a numerical value.

The `instanceUrl` and desired query field is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | confirmation of query success | success |
| count | the number of occurrences that exist in a report | 41 |
    """
    name = "Search & Replace in Report (Occurrences)"
    root = "/api/v1"
    path = f'/search-replace/occurrences'
    return request.post(base_url, headers, root+path, name, payload)

def search__replace_in_report_replace(base_url, headers, payload):
    """
    This request **finds and replaces** a value in a report, such a report title, finding title, or field key.

**NOTE:** This call can effect how a Jinja template will interact with the report if labels and keys are changed.

The `instanceUrl` and desired query field is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | confirmation of query success | success |
| data | was the data found and replaced | true |
    """
    name = "Search & Replace in Report (Replace)"
    root = "/api/v1"
    path = f'/search-replace'
    return request.post(base_url, headers, root+path, name, payload)
