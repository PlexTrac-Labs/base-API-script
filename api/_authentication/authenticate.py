from utils import request_handler as request

def authentication(base_url, headers, payload):
    """
    For more info visit: [https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview#getting-started](https://docs.plextrac.com/plextrac-documentation/master/plextrac-api-overview#getting-started)

This request **authenticates a user via a username and password**. Below is a list of information needed to fulfil the request.

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| instanceUrl | url of the Plextrac instance | example.plextrac.com |
| username | email address | [joepentester@plextrac.com](mailto:joepentester@plextrac.com) |
| password | password value | 1#$$35gg2 |

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | measurement of the authentication request | success |
| tenant_id | number that defines the PlexTrac tenant | 0 |
| cookie | value stored in browser and attached to every future request and response made to client and server to validate access | eyJhbGci... |
| token | value that uniquely identifies the user's session | eyJhbGci... |
    """
    name = "Authentication"
    root = "/api/v1"
    path = f'/authenticate'
    return request.post(base_url, headers, root+path, name, payload)

def multi_factor_authentication(base_url, headers, payload):
    """
    This request **validates access via multifactor authentication (MFA)** and requires additional verification. Below is a list of information needed to fulfil the request.

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| instanceUrl | url of the Plextrac instance | example.plextrac.com |
| code | MFA token value | {{mfaToken}} |
| token | 6-digit MFA code | 524889 |

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | measurement of the authentication request | success |
| tenant_id | number that defines the PlexTrac tenant | 0 |
| cookie | value stored in browser and attached to every future request and response made to client and server to validate access | eyJhbGci... |
| token | value that uniquely identifies the user's session | eyJhbGci... |
    """
    name = "Multi-Factor Authentication"
    root = "/api/v1"
    path = f'/authenticate/mfa'
    return request.post(base_url, headers, root+path, name, payload)
