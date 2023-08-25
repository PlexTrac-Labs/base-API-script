from utils import request_handler as request

def list_all_sections(base_url, headers, payload):
    """
    This request retrieves **all sections** that exist in the **NarrativesDB** module for a tenant.
    """
    name = "List All Sections"
    root = "/api/v2"
    path = f'/narratives/sections/all'
    return request.post(base_url, headers, root+path, name, payload)

def list_narrative_repository_sections(base_url, headers, repositoryId, payload):
    """
    This request retrieves **all sections** **for a specific repository** exists in the **NarrativesDB** module.
    """
    name = "List Narrative Repository Sections"
    root = "/api/v2"
    path = f'/narratives/{repositoryId}/sections'
    return request.post(base_url, headers, root+path, name, payload)

def get_narrative_repository_section(base_url, headers, sectionId):
    """
    This request retrieves **a specific section** that exist in the **NarrativesDB** module.
    """
    name = "Get Narrative Repository Section"
    root = "/api/v2"
    path = f'/narratives/sections/{sectionId}'
    return request.get(base_url, headers, root+path, name)

def create_narrativesdb_repository(base_url, headers, payload):
    """
    This request **creates a NarrativesDB repository** that is put in the **NarrativesDB** module of the **Content Library**.
    """
    name = "Create NarrativesDB Repository"
    root = "/api/v2"
    path = f'/narratives/createNarrativesRepository'
    return request.post(base_url, headers, root+path, name, payload)

def create_narratives_repository_section(base_url, headers, payload):
    """
    This request **creates a section** in the **NarrativesDB** module of the **Content Library**.
    """
    name = "Create Narratives Repository Section"
    root = "/api/v2"
    path = f'/narratives/sections'
    return request.post(base_url, headers, root+path, name, payload)

def update_narrativedb_section(base_url, headers, sectionId, payload):
    """
    This request **updates** **a section** that exists in the **NarrativesDB** module.
    """
    name = "Update NarrativeDB Section"
    root = "/api/v2"
    path = f'/narratives/sections/{sectionId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_narrativedb_section(base_url, headers, repositoryId, sectionId):
    """
    This request deletes **a section from a specific repository** in the **NarrativesDB** module.
    """
    name = "Delete NarrativeDB Section"
    root = "/api/v2"
    path = f'/narratives/{repositoryId}/sections/{sectionId}'
    return request.delete(base_url, headers, root+path, name)

def list_narrativedbs(base_url, headers, payload):
    """
    This request **retrieves a list of all repositories** that is in the **NarrativesDB** module of the **Content Library** based on the user making the call and the permissionsLevel body param.
    """
    name = "List NarrativeDBs"
    root = "/api/v2"
    path = f'/narratives/getAllNarrativesRepositories'
    return request.post(base_url, headers, root+path, name, payload)

def copy_section_to_narative_repository(base_url, headers, payload):
    """
    This request **copies a section** **to another repository** in the **NarrativesDB** module.
    """
    name = "Copy Section to Narative Repository"
    root = "/api/v2"
    path = f'/narratives/sections/copy'
    return request.post(base_url, headers, root+path, name, payload)
