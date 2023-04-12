from utils import request_handler as request

def list_questionnaires(base_url, headers, tenantId):
    """
    This request retrieves **all** assessments for a tenant.

The `instanceUrl` and `tenantId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| questionniare_id | ID of assessment | 1345 |
| assessment_title | title of assessment | CIS Control 12: Boundary Defense |
| framework | framework that questionnaire was assessed against | cis20 |
    """
    name = "List Questionnaires"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/assessments'
    return request.get(base_url, headers, root+path, name)

def delete_questionnaire(base_url, headers, tenantId, questionnaireId):
    """
    This request **removes** an assessment from a tenant.

The `instanceUrl`, `tenantId`, and `questionnaireId` is needed to execute the call.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | validation of delete request | success |
| message | explanation of request | Questionnaire 0 deleted successfully! |
    """
    name = "Delete Questionnaire"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/assessment/{questionnaireId}'
    return request.delete(base_url, headers, root+path, name)
