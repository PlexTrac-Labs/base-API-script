from utils import request_handler as request

def list_report_templates(base_url, headers, tenantId):
    """
    This request **lists all report templates** for a tenant.
    """
    name = "List Report Templates"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-templates'
    return request.get(base_url, headers, root+path, name)

def get_report_template(base_url, headers, tenantId, reportTemplateId):
    """
    This request **retrieves a specific report template** within a tenant.
    """
    name = "Get Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.get(base_url, headers, root+path, name)

def create_report_template(base_url, headers, tenantId, payload):
    """
    This request **creates** **a report template** within a tenant.
    """
    name = "Create Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template'
    return request.put(base_url, headers, root+path, name, payload)

def update_report_template(base_url, headers, tenantId, reportTemplateId, payload):
    """
    This request **updates** **a report template** within a tenant.
    """
    name = "Update Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_report_template(base_url, headers, tenantId, reportTemplateId):
    """
    No description in Postman
    """
    name = "Delete Report Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/report-template/{reportTemplateId}'
    return request.delete(base_url, headers, root+path, name)
