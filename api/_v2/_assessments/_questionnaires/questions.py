from utils import request_handler as request

def list_questions(base_url, headers, questionnaireId, limit, offset, search):
    """
    This request **retrieves** all questions that exist for a specific questionnaire.

    Query Parameters:
    limit: (number, default: 50) pagination limit - example (50)
    offset: (number, default: 0) pagination offset - example (0)
    search: (string) seach in question title: %title% - example (form)
    """
    name = "List Questions"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions?limit={limit}?offset={offset}?search={search}'
    return request.get(base_url, headers, root+path, name)

def get_question(base_url, headers, questionnaireId, questionId):
    """
    This request **retrieves** **a specific** question from a specific questionnaire.
    """
    name = "Get Question"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions/{questionId}'
    return request.get(base_url, headers, root+path, name)

def create_question(base_url, headers, questionnaireId, payload):
    """
    This request **creates a question** for a specific questionnaire.
    """
    name = "Create Question"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions'
    return request.post(base_url, headers, root+path, name, payload)

def update_question(base_url, headers, questionnaireId, questionId, payload):
    """
    This request **updates** a questions that exists for a specific questionnaire.

{  
"answer_type": "multiSelect",  
"category": "Protection",  
"recommendations": "recommendation",  
"references": "refenreces",  
"score": {  
"calculation": "ccv",  
"value": ""  
},  
"severity": "High",  
"text": "xxxx",  
"title": "Yes (Fail) / No (Pass) II",  
"order": 2,  
"tags": \["questionnaire_xyz", "asset-tag", "c", "questionnaire_abc", "in"\],  
"multi_choice_answers": \[  
{"answer": "test"},  
{"answer": "test 1"}  
\],  
"write_up": "template_10377836",  
"custom_fields": \[{  
"key": "1",  
"label": "Custom Field",  
"value": "foo"  
},{  
"key": "2",  
"label": "Custom Field 2",  
"value": "bar"  
}\]  
}
    """
    name = "Update Question"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions/{questionId}'
    return request.put(base_url, headers, root+path, name, payload)

def change_question_order(base_url, headers, questionnaireId, questionId, payload):
    """
    This request **changes the order** of a specific question for a specific questionnaire.
    """
    name = "Change Question Order"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions/{questionId}/order'
    return request.put(base_url, headers, root+path, name, payload)

def delete_question(base_url, headers, questionnaireId, questionId):
    """
    This request **deletes** a specific question for a specific questionnaire.
    """
    name = "Delete Question"
    root = "/api/v2"
    path = f'/assessments/questionnaires/{questionnaireId}/questions/{questionId}'
    return request.delete(base_url, headers, root+path, name)
