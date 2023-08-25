from utils import request_handler as request

def list_answer_types(base_url, headers, tenantId, clientId, payload):
    """
    This request **retrieves** **all answer types** that exist for a client.

Can use the `clientId` of `0` to return all answer types in the tenant.
    """
    name = "List Answer Types"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/answertypes'
    return request.post(base_url, headers, root+path, name, payload)

def get_answer_type(base_url, headers, tenantId, clientId, answerTypeId):
    """
    This request **retrieves a specific answer type** using `answerTypeId`.
    """
    name = "Get Answer Type"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'
    return request.get(base_url, headers, root+path, name)

def update_answer_type(base_url, headers, tenantId, clientId, answerTypeId, payload):
    """
    This request **updates a specific answer type** for a specific client using `answerTypeId`.
    """
    name = "Update Answer Type"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'
    return request.put(base_url, headers, root+path, name, payload)

def create_answer_type(base_url, headers, tenantId, clientId, payload):
    """
    This request **creates an answer** for a specific client.
    """
    name = "Create Answer Type"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/answertypes/create'
    return request.post(base_url, headers, root+path, name, payload)

def delete_answer_type(base_url, headers, tenantId, clientId, answerTypeId):
    """
    This request **deletes a specific answer type** for a specific client using `answerTypeId`.
    """
    name = "Delete Answer Type"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/client/{clientId}/answertypes/{answerTypeId}'
    return request.delete(base_url, headers, root+path, name)
