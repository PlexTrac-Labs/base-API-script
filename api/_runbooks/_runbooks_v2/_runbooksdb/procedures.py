from utils import request_handler as request

def runbookprocedurelistv2(base_url, headers, payload):
    """
    Returns a list of Procedures in the RunbooksDB
    """
    name = "RunbookProcedureListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookproceduredetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Procedure
    """
    name = "RunbookProcedureDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookprocedurecreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookProcedureCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookprocedureupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookProcedureUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookproceduredeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookProcedureDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
