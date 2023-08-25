from utils import request_handler as request

def runbookengagementprocedurelogsv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureLogsV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedurelogcreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureLogCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedurelogupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureLogUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedurelogdeletev2(base_url, headers, payload):
    """
    team can be one of "RED", "BLUE"
    """
    name = "RunbookEngagementProcedureLogDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
