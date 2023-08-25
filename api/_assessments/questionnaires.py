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

def get_questionnaire(base_url, headers, questionnaireId, payload):
    """
    This request retrieves a specific questionnaire from the **Assessments** module.
    """
    name = "Get Questionnaire"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}'
    return request.get(base_url, headers, root+path, name, payload)

def create_questionnaire(base_url, headers, payload):
    """
    This request **creates** a questionnaire to be stored in the **Assessments** module.
    """
    name = "Create Questionnaire"
    root = "/api/v2"
    path = f'/assessments/questionnaires'
    return request.post(base_url, headers, root+path, name, payload)

def update_questionnaire(base_url, headers, questionnaireId, payload):
    """
    This request **updates** information for a specific questionnaire in the **Assessments** module.
    """
    name = "Update Questionnaire"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}'
    return request.put(base_url, headers, root+path, name, payload)

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

def export_questionnaire(base_url, headers, questionnaireId, payload):
    """
    This request **exports** a specific questionnaire from the **Assessments** module.
    """
    name = "Export Questionnaire"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/export'
    return request.get(base_url, headers, root+path, name, payload)

def import_questionnaire(base_url, headers, payload):
    """
    This request imports a questionnaire to the **Assessments** module.
    """
    name = "Import Questionnaire"
    root = "/api/v2"
    path = f'/import/questionnaire'
    return request.post(base_url, headers, root+path, name, payload)
