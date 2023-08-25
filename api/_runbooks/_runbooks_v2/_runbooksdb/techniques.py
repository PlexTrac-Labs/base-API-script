from utils import request_handler as request

def runbooktechniquelistv2(base_url, headers, payload):
    """
    StartFragment

Returns a list of Techniques in the RunbooksDB
    """
    name = "RunbookTechniqueListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktechniquedetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Technique
    """
    name = "RunbookTechniqueDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktechniquecreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTechniqueCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktechniqueupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTechniqueUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooktechniquedeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookTechniqueDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
