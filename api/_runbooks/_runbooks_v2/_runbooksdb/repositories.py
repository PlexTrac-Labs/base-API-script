from utils import request_handler as request

def runbookrepositorylistv2(base_url, headers, payload):
    """
    Returns a list of all Repositories in the RunbooksDB
    """
    name = "RunbookRepositoryListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositorydetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Repository and a list of Procedures it contains
    """
    name = "RunbookRepositoryDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositorycreatev2(base_url, headers, payload):
    """
    Create a RunbookDB Repository.

Must have a unique `shortName` (`Repository ID Prefix` in platform)

`type` can be one of `["private", "managed", "open"]`
    """
    name = "RunbookRepositoryCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositoryupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookrepositorydeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookRepositoryDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
