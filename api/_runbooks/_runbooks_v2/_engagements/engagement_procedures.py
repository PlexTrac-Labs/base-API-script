from utils import request_handler as request

def runbookengagementprocedureidsv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureIdsV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedurelistv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementproceduredetailv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementproceduredeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
