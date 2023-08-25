from utils import request_handler as request

def runbookengagementprocedureattachmentlistv2(base_url, headers, payload):
    """
    team can be one of "RED", "BLUE"
    """
    name = "RunbookEngagementProcedureAttachmentListV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def upload_attachment_to_engagement_procedure(base_url, headers, engagementProcedureId, payload):
    """
    REST endpoint to upload attachments to a RunbooksV2 Engagment Procedure
    """
    name = "Upload Attachment to Engagement Procedure"
    root = "/api/v2"
    path = f'/runbooks/engagement-procedures/{engagementProcedureId}/attachments/upload'
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureattachmentsupdatev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureAttachmentsUpdateV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)

def runbookengagementprocedureattachmentdeletev2(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "RunbookEngagementProcedureAttachmentDeleteV2"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
