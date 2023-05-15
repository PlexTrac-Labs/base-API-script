from utils import request_handler as request

def get_all_narrativedb_users(base_url, headers, payload):
    """
    This request **retrieves** **all users** that have been added to repositories in the **NarrativesDB** module.

Users can be added in the platform by admins via the "Users & Permissions" option on the **Repositories** tab of **NarrativesDB**.
    """
    name = "Get All NarrativeDB Users"
    root = "/api/v2"
    path = f'/narratives/users/all'
    return request.post(base_url, headers, root+path, name, payload)

def get_narrativedb_users_by_repository(base_url, headers, narrativeRepositoryId, payload):
    """
    This request **retrieves users** for **a specific repository** in the **NarrativesDB** module.

Users can be added in the platform by admins via the "Users & Permissions" option on the **Repositories** tab of **NarrativesDB**.
    """
    name = "Get NarrativeDB Users by Repository"
    root = "/api/v2"
    path = f'/narratives/{narrativeRepositoryId}/users'
    return request.post(base_url, headers, root+path, name, payload)

def update_narrativedb_users_by_repository(base_url, headers, narrativeRepositoryId, payload):
    """
    This request **adds users** to a specific repository in the **NarrativesDB** module.

Only Standard users need to be added, as Admins have access to all repositories.

When replace is set to **TRUE** the repositoryUsers list replaces the previous list. When set to **FALSE**, it acts as an upsert and will add new users or modify existing users.

For example:

*   Use replace is TRUE when one user exists who no longer needs access and two different users need to be added. If replace is set to TRUE, the final list will only contain the two new users and the first user will no longer have access.
*   Use replace is FALSE when one user currently has access and should continue access, but two more users need access. If replace is set to FALSE, the final list will contain three users.
    

Users can be added in the platform by admins via the "Users & Permissions" option on the **Repositories** tab of **NarrativesDB**.
    """
    name = "Update NarrativeDB Users by Repository"
    root = "/api/v2"
    path = f'/narratives/{narrativeRepositoryId}/users'
    return request.put(base_url, headers, root+path, name, payload)
