from utils import request_handler as request

def findingupdate(base_url, headers, payload):
    """
    Update individual properties on a finding.

StartFragment

**NOTE:** The Custom Fields tab of a finding in the platform is considered a single property.

``` json
"data": {
    "fields": [
        {
            "key": "synopsis",
            "label": "Synopsis",
            "value": "The remote OS or service pack is no longer supported. test"
        },
        {
            "key": "evidence",
            "label": "Evidence",
            "value": ""
        }
    ]
}

```

This means to update to any custom field key, label, or value you will need to send the entire `fields` object in the `data` property.

EndFr
    """
    name = "FindingUpdate"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
