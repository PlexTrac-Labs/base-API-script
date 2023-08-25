from utils import request_handler as request

def list_findings_templates(base_url, headers):
    """
    This request **lists all findings templates** for a tenant.
    """
    name = "List Findings Templates"
    root = "/api/v1"
    path = f'/field-templates'
    return request.get(base_url, headers, root+path, name)

def get_findings_template(base_url, headers, findingTemplateId):
    """
    This request retrieves **a findings template**
    """
    name = "Get Findings Template"
    root = "/api/v1"
    path = f'/field-template/{findingTemplateId}'
    return request.get(base_url, headers, root+path, name)

def create_finding_template(base_url, headers, tenantId, payload):
    """
    This request **creates** **a findings template** within a tenant.
    """
    name = "Create Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template'
    return request.put(base_url, headers, root+path, name, payload)

def update_finding_template(base_url, headers, tenantId, findingTemplateId, payload):
    """
    Update a finding template in your tenancy
    """
    name = "Update Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template/{findingTemplateId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_finding_template(base_url, headers, tenantId, findingTemplateId):
    """
    No description in Postman
    """
    name = "Delete Finding Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/field-template/{findingTemplateId}'
    return request.delete(base_url, headers, root+path, name)
