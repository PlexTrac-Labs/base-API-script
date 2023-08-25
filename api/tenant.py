from utils import request_handler as request

def get_tenant(base_url, headers, tenantId):
    """
    This request **obtains information about a tenant**, such as ID, settings, point of contact information, etc.
    """
    name = "Get Tenant"
    root = "/api/v1"
    path = f'/tenant/{tenantId}'
    return request.get(base_url, headers, root+path, name)

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

def add_tenant_logo(base_url, headers, tenantId, payload):
    """
    Add a logo for your tenancy
    """
    name = "Add Tenant Logo"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo'
    return request.post(base_url, headers, root+path, name, payload)

def add_tenant_logo_dark(base_url, headers, tenantId, payload):
    """
    Add a logo for your tenancy
    """
    name = "Add Tenant Logo Dark"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo/dark'
    return request.post(base_url, headers, root+path, name, payload)

def delete_tenant_logo(base_url, headers, tenantId):
    """
    Remove the logo from your tenancy. This action will result in the PlexTrac logo being displayed.
    """
    name = "Delete Tenant Logo"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo'
    return request.delete(base_url, headers, root+path, name)

def delete_tenant_logo_dark(base_url, headers, tenantId):
    """
    Remove the logo from your tenancy. This action will result in the PlexTrac logo being displayed.
    """
    name = "Delete Tenant Logo Dark"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/logo/dark'
    return request.delete(base_url, headers, root+path, name)

def delete_tenant_icon(base_url, headers, tenantId):
    """
    No description in Postman
    """
    name = "Delete Tenant Icon"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/icon'
    return request.delete(base_url, headers, root+path, name)

def delete_tenant_icon_dark(base_url, headers, tenantId):
    """
    No description in Postman
    """
    name = "Delete Tenant Icon Dark"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/icon/dark'
    return request.delete(base_url, headers, root+path, name)

def root_request(base_url, headers):
    """
    Root request. You can determine that the instance is up and running if this request returns the following JSON

``` json
{
    "text": "Authenticate at /authenticate"
}

```
    """
    name = "Root Request"
    root = "/api/v1"
    path = f'/'
    return request.get(base_url, headers, root+path, name)
