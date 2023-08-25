from utils import request_handler as request

def runbooktacticlistv2(base_url, headers, payload):
    """
    Returns a list of Tactics in the RunbooksDB
    """
    name = "RunbookTacticListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktacticdetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Tactic
    """
    name = "RunbookTacticDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktacticcreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTacticCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktacticupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTacticUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktacticdeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTacticDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
