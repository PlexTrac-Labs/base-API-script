from utils import request_handler as request

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
