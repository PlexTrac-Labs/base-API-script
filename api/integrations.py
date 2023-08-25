from utils import request_handler as request

def get_configurations(base_url, headers):
    """
    No description in Postman
    """
    name = "Get Configurations"
    root = "/api/v2"
    path = f'/integrations/configurations'
    return request.get(base_url, headers, root+path, name)

def create_configurations(base_url, headers, payload):
    """
    Creates a config for an integration.

`integrationType` can be one of:

- Colbalt
- HackerOne
- MSV
- Snyk
    

`apiUserName` and `orgId` are allowed to be an empty string if they don't exist for your integration.
    """
    name = "Create Configurations"
    root = "/api/v2"
    path = f'/integrations/configurations'
    return request.post(base_url, headers, root+path, name, payload)

def get_configuration(base_url, headers, configId):
    """
    Creates a config for an integration.

`integrationType` can be one of:

- Colbalt
- HackerOne
- MSV
- Snyk
    

`apiUserName` and `orgId` are allowed to be an empty string if they don't exist for your integration.
    """
    name = "Get Configuration"
    root = "/api/v2"
    path = f'/integrations/configurations/{configId}'
    return request.get(base_url, headers, root+path, name)

def update_configuration(base_url, headers, configId, payload):
    """
    Creates a config for an integration.

`integrationType` can be one of:

- Colbalt
- HackerOne
- MSV
- Snyk
    

`apiUserName` and `orgId` are allowed to be an empty string if they don't exist for your integration.
    """
    name = "Update Configuration"
    root = "/api/v2"
    path = f'/integrations/configurations/{configId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_configuration(base_url, headers, configId):
    """
    Creates a config for an integration.

`integrationType` can be one of:

- Colbalt
- HackerOne
- MSV
- Snyk
    

`apiUserName` and `orgId` are allowed to be an empty string if they don't exist for your integration.
    """
    name = "Delete Configuration"
    root = "/api/v2"
    path = f'/integrations/configurations/{configId}'
    return request.delete(base_url, headers, root+path, name)
