from utils import request_handler as request

def runbookengagementprocedureassetlistv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureAssetListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureassetsaddv2(base_url, headers, payload):
    """
    Add an existing asset to a procedure in a RunbookV2 engagement.
    """
    name = "RunbookEngagementProcedureAssetsAddV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureassetcreatev2(base_url, headers, payload):
    """
    Create a new asset and add it to a procedure in a RunbookV2 engagement.
    """
    name = "RunbookEngagementProcedureAssetCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureassetdeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureAssetDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureassetupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureAssetUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
