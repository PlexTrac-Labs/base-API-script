from utils import request_handler as request

def get_narrativedb(base_url, headers, narrativeRepositoryId):
    """
    This request **retrieves a specific repository** and its metadata from the **NarrativesDB** module.
    """
    name = "Get NarrativeDB"
    root = "/api/v2"
    path = f'/narratives/{narrativeRepositoryId}/getNarrativesRepository'
    return request.get(base_url, headers, root+path, name)

def update_narrativedb(base_url, headers, narrativeRepositoryId, payload):
    """
    This request **updates a specific repository** and its metadata from the **NarrativesDB** module.
    """
    name = "Update NarrativeDB"
    root = "/api/v2"
    path = f'/narratives/{narrativeRepositoryId}/updateNarrativesRepository'
    return request.put(base_url, headers, root+path, name, payload)

def delete_narrativedb(base_url, headers, narrativeRepositoryId):
    """
    This request **deletes a specific repository** from the **NarrativesDB** module.
    """
    name = "Delete NarrativeDB"
    root = "/api/v2"
    path = f'/narratives/{narrativeRepositoryId}/deleteNarrativesRepository'
    return request.delete(base_url, headers, root+path, name)
