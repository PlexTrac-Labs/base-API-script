from utils import request_handler as request

def runbooktestplanlistv2(base_url, headers, payload):
    """
    Returns a list of RunbookV2 Test Plans
    """
    name = "RunbookTestPlanListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktestplandetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Test Plan and all Procedures it contains
    """
    name = "RunbookTestPlanDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktestplancreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTestPlanCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktestplanupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTestPlanUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktestplandeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTestPlanDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
