from utils import request_handler as request

def get_authenticated_user(base_url, headers):
    """
    This request **retrieves information** about the user executing the endpoint, such as name, admin status, role, tenant ID, user ID, etc.
    """
    name = "Get Authenticated User"
    root = "/api/v1"
    path = f'/user/whoami'
    return request.get(base_url, headers, root+path, name)

def update_user(base_url, headers, payload):
    """
    This request **updates information** about the user executing the endpoint.
    """
    name = "Update User"
    root = "/api/v1"
    path = f'/user/update'
    return request.put(base_url, headers, root+path, name, payload)

def change_password(base_url, headers, payload):
    """
    This request **changes the password** for an existing user.
    """
    name = "Change Password"
    root = "/api/v1"
    path = f'/user/changepass'
    return request.put(base_url, headers, root+path, name, payload)

def forgot_password(base_url, headers, payload):
    """
    This request **sends a password recovery email** to an existing user based on the email address provided in the query.
    """
    name = "Forgot Password"
    root = "/api/v1"
    path = f'/user/forgotpass'
    return request.post(base_url, headers, root+path, name, payload)

def set_mfa_token(base_url, headers):
    """
    This request **sets the multi-factor authentication token** of the current authenticated user.
    """
    name = "Set MFA Token"
    root = "/api/v1"
    path = f'/user/mfa/token'
    return request.put(base_url, headers, root+path, name)

def disable_mfa_token(base_url, headers):
    """
    This request **disables the multi-factor authentication token** of the current authenticated user.
    """
    name = "Disable MFA Token"
    root = "/api/v1"
    path = f'/user/mfa/token/disable'
    return request.put(base_url, headers, root+path, name)

def get_user_notifications(base_url, headers, limit, skip, read):
    """
    This request **retrieves notifications** for the current authenticated user.

    Query Parameters:
    limit: Integer: Num notifications to return. Default 10 - example (10)
    skip: Integer: Index of notifications to skip. Default 0 - example (0)
    read: 'read', 'unread', 'any' - example (any)
    """
    name = "Get User Notifications"
    root = "/api/v1"
    path = f'/user/notifications?limit={limit}?skip={skip}?read={read}'
    return request.get(base_url, headers, root+path, name)

def update_read_notifications(base_url, headers, payload):
    """
    Update the notifications that have been read by the current authenticated user
    """
    name = "Update Read Notifications"
    root = "/api/v1"
    path = f'/user/notifications'
    return request.put(base_url, headers, root+path, name, payload)
