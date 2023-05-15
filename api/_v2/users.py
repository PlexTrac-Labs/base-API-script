from utils import request_handler as request

def get_authenticated_user(base_url, headers):
    """
    This request **retrieves user info** about the currently authenticated user.
    """
    name = "Get Authenticated User"
    root = "/api/v2"
    path = f'/whoami'
    return request.get(base_url, headers, root+path, name)

def get_user_findings(base_url, headers, payload):
    """
    This request **retrieves a list of findings assigned to the user making the API call.**
    """
    name = "Get User Findings"
    root = "/api/v2"
    path = f'/user/findings'
    return request.post(base_url, headers, root+path, name, payload)

def delete_user(base_url, headers, payload):
    """
    This request **deletes** the user associated with the email sent in the payload.
    """
    name = "Delete User"
    root = "/api/v2"
    path = f'/user/delete'
    return request.delete(base_url, headers, root+path, name, payload)
