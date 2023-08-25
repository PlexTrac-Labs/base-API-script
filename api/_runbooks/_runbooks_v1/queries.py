from utils import request_handler as request

def reportprocedure(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "reportProcedure"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def reportprocedurelist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "reportProcedureList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbook(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbook"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookcategory(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookCategory"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookcategorylist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookCategoryList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookcategorylistbydepth(base_url, headers, payload):
    """
    Returns a list of either Methodologies, Tactics or Techniques. Which list is determined by the `depth` field value:

0 - Methodologies

1 - Tactics

2 - Techniques
    """
    name = "runbookCategoryListByDepth"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookcategorylistbyparents(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookCategoryListByParents"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagement(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagement"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementavailableoperatorlist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementAvailableOperatorList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementcompletelist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementCompleteList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementlist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedure(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedure"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureassetlist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedureAssetList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureattachmentlist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedureAttachmentList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedurelist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedureList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureloglist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedureLogList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureoperatorlist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookEngagementProcedureOperatorList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooklist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbooklistv2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookprocedure(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookProcedure"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookprocedurelist(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookProcedureList"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookprocedurelistbycategoryids(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "runbookProcedureListByCategoryIds"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
