from utils import request_handler as request

def runbookengagementprocedureoperatorlistv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureOperatorListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureoperatorsupdatev2(base_url, headers, payload):
    """
    Assign a user as an operator to a procedure in a RunbookV2 engagement.
    """
    name = "RunbookEngagementProcedureOperatorsUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
