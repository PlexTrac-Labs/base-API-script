from utils import request_handler as request

def get_writeups_repository_users(base_url, headers, repositoryId):
    """
    This request **retrieves all users from a specific repository** in the **WriteupsD**B module.
    """
    name = "Get Writeups Repository Users"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/users'
    return request.get(base_url, headers, root+path, name)

def add_writeups_repository_users(base_url, headers, repositoryId, payload):
    """
    This request **adds users to a specific repository** in the **WriteupsD**B module by adding a new user entry for each user in the list sent to the endpoint.

The userId will be used to lookup a user in the Plextrac instance. That user's name and email will be used instead of the data passed into this payload.
    """
    name = "Add Writeups Repository Users"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/users'
    return request.post(base_url, headers, root+path, name, payload)

def update_writeups_repository_users(base_url, headers, repositoryId, payload):
    """
    This request **replaces the current list of users with a new one for a specific repository** in the **WriteupsD**B module.

Any users not on the list provided will be removed and no longer have access.
    """
    name = "Update Writeups Repository Users"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/users'
    return request.put(base_url, headers, root+path, name, payload)

def get_all_writeups_repository_users(base_url, headers, payload):
    """
    This request **retrieves a list of users** in the **WriteupsD**B module with the `MANAGE_WRITEUPS_REPOSITORIES` RBAC permission and returns the list filter by and user that has the `filterText` in the `first name`, `last name`, or `email` field.
    """
    name = "Get All Writeups Repository Users"
    root = "/api/v2"
    path = f'/repositories/users'
    return request.post(base_url, headers, root+path, name, payload)
