from utils import request_handler as request

def enabledisable_parser_plugin_actions(base_url, headers, tenantId, payload):
    """
    enable or disable global mapping of scanner findings to writeups
    """
    name = "Enable/Disable Parser Plugin Actions"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/integrationconfig/parserConfig'
    return request.post(base_url, headers, root+path, name, payload)

def get_tenant_parsers(base_url, headers, tenantId):
    """
    This request retrieves **a list of available parsers**.

Returned source field can be used for endpoints requiring `parserId`.
    """
    name = "Get Tenant Parsers"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions'
    return request.get(base_url, headers, root+path, name)

def get_tenant_parser_actions(base_url, headers, tenantId, parserId, limit, skip, type, query):
    """
    This request retrieves **a list of parser actions for a tenant** per identified parser source**.**

    Query Parameters:
    limit: Num of items to return - example (985)
    skip: Num of item to start on - example (0)
    type: DEFAULT, LINK, IGNORE - example (DEFAULT)
    query: Partial search of Parser Action title - example (sql)
    """
    name = "Get Tenant Parser Actions"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions/{parserId}?limit={limit}?skip={skip}?type={type}?query={query}'
    return request.get(base_url, headers, root+path, name)

def get_tenant_parser_action(base_url, headers, tenantId, parserId, actionId):
    """
    No description in Postman
    """
    name = "Get Tenant Parser Action"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions/{parserId}/action/{actionId}'
    return request.get(base_url, headers, root+path, name)

def create_tenant_parser_action(base_url, headers, tenantId, parserId, payload):
    """
    This request **creates a parser action for a tenant.**

Required fields: `id`, `severity`, `title`

`action` field: DEFAULT, LINK, IGNORE

`action` field defaults to DEFAULT when not supplied.
    """
    name = "Create Tenant Parser Action"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions/{parserId}/action'
    return request.post(base_url, headers, root+path, name, payload)

def update_parser_action(base_url, headers, tenantId, parserId, actionId, payload):
    """
    This request **updates a specific parser and specific action for a tenant.**
    """
    name = "Update Parser Action"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions/{parserId}/action/{actionId}'
    return request.put(base_url, headers, root+path, name, payload)

def bulk_update_tenant_parser_actions(base_url, headers, tenantId, parserId, payload):
    """
    This request **bulk** **updates a specific parser and specific action for a tenant.**
    """
    name = "Bulk Update Tenant Parser Actions"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/actions/{parserId}/bulk'
    return request.put(base_url, headers, root+path, name, payload)
