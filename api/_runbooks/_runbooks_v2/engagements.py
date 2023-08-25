from utils import request_handler as request

def runbookengagementlistv2(base_url, headers, payload):
    """
    Returns a list of RunbookV2 Engagements
    """
    name = "RunbookEngagementListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementdetailv2(base_url, headers, payload):
    """
    Returns the data for an In Progess Engagement
    """
    name = "RunbookEngagementDetailV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementcreatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementCreateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementdeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementfinishv2(base_url, headers, payload):
    """
    Submits a RunbookV2 Engagament and returns the ID of the created Report.
    """
    name = "RunbookEngagementFinishV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
