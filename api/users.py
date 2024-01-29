from utils import request_handler as request

def get_authenticated_user_v1(base_url, headers):
    """
    This request **retrieves information** about the user executing the endpoint, such as name, admin status, role, tenant ID, user ID, etc.
    """
    name = "Get Authenticated User v1"
    root = "/api/v1"
    path = f'/user/whoami'
    return request.get(base_url, headers, root+path, name)

def get_authenticated_user_v2(base_url, headers):
    """
    This request **retrieves user info** about the currently authenticated user.
    """
    name = "Get Authenticated User v2"
    root = "/api/v2"
    path = f'/whoami'
    return request.get(base_url, headers, root+path, name)

def list_tenant_users(base_url, headers, tenantId):
    """
    This request **retrieves a list of all users** in a tenant.
    """
    name = "List Tenant Users"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/list'
    return request.get(base_url, headers, root+path, name)

def get_tenants_users(base_url, headers, tenantId, offset, limit, sortBy, order, filter):
    """
    This request **retrieves a paginated list of all users** in a tenant.

    Query Parameters:
    offset: optional: number of user records to offset pagination by - example (0)
    limit: optional: number of users to limit in pagination results - example (10)
    sortBy: optional: avilable 'firstName', 'lastName', 'email' - example (firstName)
    order: optional: available 'DESCEND', 'ASCEND' - example (DESEND)
    filter: optional: value to do a partial match to a user's name - example (None)
    """
    name = "Get Tenants Users"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/users?offset={offset}?limit={limit}?sortBy={sortBy}?order={order}?filter={filter}'
    return request.get(base_url, headers, root+path, name)

def create_user_deprecated(base_url, headers, tenantId, payload):
    """
    Create a new user in your tenant

**This route is deprecated and will be blocked in a future release, please now call:{domain}/tenant/{tenantId}/user/create/bulk**
    """
    name = "Create User (DEPRECATED)"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_create_user(base_url, headers, tenantId, payload):
    """
    Create new users in your tenant.

`role` can be one of the defaults "ADMIN", "STD_USER", or "ANALYST". For custom RBAC roles you need to find the `key` for your custom role. Then the use the pattern TENANT_\[tenant ID\]_ROLE_\[key of custom RBAC role\] e.g. "TENANT_0_ROLE_MY_CUSTOM_ROLE"
    """
    name = "Bulk Create User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/create/bulk'
    return request.post(base_url, headers, root+path, name, payload)

def update_user(base_url, headers, payload):
    """
    This request **updates information** about the user executing the endpoint.
    """
    name = "Update User"
    root = "/api/v1"
    path = f'/user/update'
    return request.put(base_url, headers, root+path, name, payload)

def delete_user(base_url, headers, payload):
    """
    This request **deletes** the user associated with the email sent in the payload.
    """
    name = "Delete User"
    root = "/api/v2"
    path = f'/user/delete'
    return request.delete(base_url, headers, root+path, name, payload)

def change_password(base_url, headers, payload):
    """
    This request **changes the password** for the user making the request. You cannot change another users password.
    """
    name = "Change Password"
    root = "/api/v1"
    path = f'/user/changepass'
    return request.put(base_url, headers, root+path, name, payload)

def forgot_password(base_url, headers, payload):
    """
    This request **sends a password recovery email** to an existing user based on the email address provided in the query.

This endpoint doesn't require authenication.
    """
    name = "Forgot Password"
    root = "/api/v1"
    path = f'/user/forgotpass'
    return request.post(base_url, headers, root+path, name, payload)

def reset_user_password(base_url, headers, tenantId, payload):
    """
    Send an email for a user to reset their password.
    """
    name = "Reset User Password"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/resetpass'
    return request.put(base_url, headers, root+path, name, payload)

def set_mfa_token(base_url, headers):
    """
    This request **sets the multi-factor authentication token** of the current authenticated user.
    """
    name = "Set MFA Token"
    root = "/api/v1"
    path = f'/user/mfa/token'
    return request.put(base_url, headers, root+path, name)

def disable_user_mfa_token(base_url, headers):
    """
    This request **disables the multi-factor authentication token** of the current authenticated user.
    """
    name = "Disable User MFA Token"
    root = "/api/v1"
    path = f'/user/mfa/token/disable'
    return request.put(base_url, headers, root+path, name)

def disable_other_user_mfa_token(base_url, headers, tenantId, payload):
    """
    Disable MFA for an authorized user in your tenant
    """
    name = "Disable Other User MFA Token"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/mfa/disable'
    return request.put(base_url, headers, root+path, name, payload)

def enabledisable_user(base_url, headers, tenantId, payload):
    """
    Toggles the **User Disabled** switch shown in the Admin Dashboard > Users. This enables or disables a user from authenticating to the platform.
    """
    name = "Enable/Disable User"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/user/toggledisabled'
    return request.post(base_url, headers, root+path, name, payload)

def get_user_notifications(base_url, headers, limit, skip, read):
    """
    This request **retrieves notifications** for the current authenticated user.

    Query Parameters:
    limit: Integer: Num notifications to return. Default 10 - example (10)
    skip: Integer: Index of notifications to skip. Default 0 - example (0)
    read: 'read', 'unread', 'any' - example (unread)
    """
    name = "Get User Notifications"
    root = "/api/v1"
    path = f'/user/notifications?limit={limit}?skip={skip}?read={read}'
    return request.get(base_url, headers, root+path, name)

def set_user_notifications_read(base_url, headers, payload):
    """
    Mark a notification as read by the user.
    """
    name = "Set User Notifications Read"
    root = "/api/v1"
    path = f'/user/notifications'
    return request.put(base_url, headers, root+path, name, payload)

def get_user_findings(base_url, headers, payload):
    """
    This request **retrieves a list of findings assigned to the user making the API call.**
    """
    name = "Get User Findings"
    root = "/api/v2"
    path = f'/user/findings'
    return request.post(base_url, headers, root+path, name, payload)
