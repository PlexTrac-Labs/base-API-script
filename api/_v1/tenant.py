from utils import request_handler as request

def update_tenant(base_url, headers, tenantId, name, address, poc):
    """
    Update the details of your tenant, including `name`, `address`, and `point of contact`

    Query Parameters:
    name: The name of the tenant - example (Me!)
    address: The address of the tenant - example (string)
    poc: The point of contact object that includes `first`, `last`, and `email` - example (object)
    """
    name = "Update Tenant"
    root = "/api/v1"
    path = f'/tenant/{tenantId}?name={name}?address={address}?poc={poc}'
    return request.put(base_url, headers, root+path, name)

def get_tenant(base_url, headers, tenantId):
    """
    This request **obtains information about a tenant**, such as ID, settings, point of contact information, etc.
    """
    name = "Get Tenant"
    root = "/api/v1"
    path = f'/tenant/{tenantId}'
    return request.get(base_url, headers, root+path, name)

def get_notification_settings(base_url, headers, tenantId):
    """
    This request **retrieves the number of days to wait** before reminding users to provide status updates on assigned findings.
    """
    name = "Get Notification Settings"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/notificationsettings'
    return request.get(base_url, headers, root+path, name)

def update_notification_settings(base_url, headers, tenantId, reminderDays):
    """
    Update the number of days to wait before reminding users to provide status updates on findings assigned to them

    Query Parameters:
    reminderDays: The number of days before users receive notifications to provide status updates - example (number)
    """
    name = "Update Notification Settings"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/notificationsettings?reminderDays={reminderDays}'
    return request.put(base_url, headers, root+path, name)

def tenant_analytics(base_url, headers, tenantId):
    """
    This request retrieves **analytics for a tenant,** providing a total count of findings by risk and status.
    """
    name = "Tenant Analytics"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/analytics'
    return request.get(base_url, headers, root+path, name)

def list_tenant_users(base_url, headers, tenantId):
    """
    This request **retrieves a list of all users** in a tenant.
    """
    name = "List Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/list'
    return request.get(base_url, headers, root+path, name)

def list_tenant_tags(base_url, headers, tenantId, limit, offset):
    """
    This request retrieves **a list of all tags for a tenant** with filter options.

    Query Parameters:
    limit: No description in Postman - example (10)
    offset: No description in Postman - example (0)
    """
    name = "List Tenant Tags"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag?limit={limit}?offset={offset}'
    return request.get(base_url, headers, root+path, name)

def list_tenant_clients(base_url, headers, tenantId):
    """
    List all clients of a given tenant
    """
    name = "List Tenant Clients"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/list'
    return request.get(base_url, headers, root+path, name)

def disable_multifactor_authentication(base_url, headers, tenantId, email):
    """
    Disable MFA for an authorized user in your tenant

    Query Parameters:
    email: The email of the user for whom to disable MFA - example (string)
    """
    name = "Disable Multifactor Authentication"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/mfa/disable?email={email}'
    return request.put(base_url, headers, root+path, name)

def reset_user_password(base_url, headers, tenantId, payload):
    """
    Generate a new 20-character password for a given user
    """
    name = "Reset User Password"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/resetpass'
    return request.put(base_url, headers, root+path, name, payload)

def add_logo(base_url, headers, tenantId, payload):
    """
    Add a logo for your tenancy
    """
    name = "Add Logo"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo'
    return request.post(base_url, headers, root+path, name, payload)

def create_user_deprecated(base_url, headers, tenantId, payload):
    """
    Create a new user in your tenant

**This route is deprecated and will be blocked in a future release, please now call:{domain}/tenant/{tenantId}/user/create/bulk**
    """
    name = "Create User (DEPRECATED)"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create'
    return request.post(base_url, headers, root+path, name, payload)

def create_user(base_url, headers, tenantId, payload):
    """
    Create a new user in your tenant
    """
    name = "Create User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create/bulk'
    return request.post(base_url, headers, root+path, name, payload)

def enabledisable_user(base_url, headers, tenantId, payload):
    """
    Toggle a user's authorization to your tenancy
    """
    name = "Enable/Disable User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/toggledisable'
    return request.post(base_url, headers, root+path, name, payload)

def delete_logo(base_url, headers, tenantId):
    """
    Remove the logo from your tenancy. This action will result in the PlexTrac logo being displayed.
    """
    name = "Delete Logo"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo'
    return request.delete(base_url, headers, root+path, name)

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

def change_parser_integration_config(base_url, headers, tenantId, payload):
    """
    enable or disable global mapping of scanner findings to writeups
    """
    name = "Change parser integration config"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/integrationconfig/parserConfig'
    return request.post(base_url, headers, root+path, name, payload)
