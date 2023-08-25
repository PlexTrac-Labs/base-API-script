from utils import request_handler as request

def runbookrepositoryavailableuserlistv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryAvailableUserListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositoryusersv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryUsersV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositoryusersaddv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryUsersAddV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositoryuserupdatev2(base_url, headers, payload):
    """
    Can update the permission of a user in the RunbookDB Repository.

`role` can be one of `["viewer", "editor"]`
    """
    name = "RunbookRepositoryUserUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositoryuserremovev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryUserRemoveV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
