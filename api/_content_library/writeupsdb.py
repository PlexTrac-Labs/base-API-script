from utils import request_handler as request

def list_all_writeup_repositories(base_url, headers, payload):
    """
    This request **retrieves a list of repositories** in the **WriteupsD**B module.

Must send an empty JSON object with the request.
    """
    name = "List All Writeup Repositories"
    root = "/api/v2"
    path = f'/repositories/getAllWriteupsRepositories'
    return request.post(base_url, headers, root+path, name, payload)

def get_writeups_repository_users_can_edit(base_url, headers):
    """
    If the user has the RBAC permission `ACCESS_WRITEUPS_REPOSITORIES`, this request **retrieves a list of repositories** in the **WriteupsD**B module that the user is assigned an EDITOR on.
    """
    name = "Get Writeups Repository Users Can Edit"
    root = "/api/v2"
    path = f'/repositories/listUserCanEdit'
    return request.get(base_url, headers, root+path, name)

def get_writeup_repository(base_url, headers, repositoryId, payload):
    """
    This request **retrieves a specific repository and associated metadata** in the **WriteupsDB** module.

The `repositoryID` is found in the url when viewing the repository:

1.  Open PlexTrac.
2.  Expand "Content Library" pulldown in the main menu.
3.  Click **WriteupsDB**.
4.  Click the desired repository.
5.  Inspect the url. It is the value between "repository" and "writeups."
    

.../repository/**cl0e3lc0c002318mx4y2bg3wn**/writeups
    """
    name = "Get Writeup Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}'
    return request.post(base_url, headers, root+path, name, payload)

def create_writeup_repository(base_url, headers, payload):
    """
    This request **adds a new repository** in the **WriteupsDB** module.
    """
    name = "Create Writeup Repository"
    root = "/api/v2"
    path = f'/repositories/add'
    return request.post(base_url, headers, root+path, name, payload)

def update_writeup_repository(base_url, headers, repositoryId, payload):
    """
    This request **updates a specific repository and associated metadata** in the **WriteupsDB** module.

The `repositoryID` is found in the url when viewing the repository:

1.  Open PlexTrac.
2.  Expand "Content Library" pulldown in the main menu.
3.  Click **WriteupsDB**.
4.  Click the desired repository.
5.  Inspect the url. It is the value between "repository" and "writeups."
    

.../repository/**cl0e3lc0c002318mx4y2bg3wn**/writeups
    """
    name = "Update Writeup Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/update'
    return request.post(base_url, headers, root+path, name, payload)

def delete_writeup_repository(base_url, headers, payload):
    """
    This request **deletes a repository** in the **WriteupsDB** module.
    """
    name = "Delete Writeup Repository"
    root = "/api/v2"
    path = f'/repositories/delete'
    return request.post(base_url, headers, root+path, name, payload)
