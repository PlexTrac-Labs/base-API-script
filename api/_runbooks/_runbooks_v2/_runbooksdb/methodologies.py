from utils import request_handler as request

def runbookmethodologylistv2(base_url, headers, payload):
    """
    Returns a list of Methodologies in the RunbooksDB
    """
    name = "RunbookMethodologyListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookmethodologydetailv2(base_url, headers, payload):
    """
    Returns the data for a RunbooksV2 Methodology
    """
    name = "RunbookMethodologyDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookmethodologycreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookMethodologyCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookmethodologyupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookMethodologyUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookmethodologydeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookMethodologyDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
