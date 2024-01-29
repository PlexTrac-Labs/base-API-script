from utils import request_handler as request

def list_export_templates(base_url, headers, tenantId):
    """
    Returns a list of all Export Templates in the tenant.

Please see our public docs for more information about how [Export Templates](https://docs.plextrac.com/plextrac-documentation/product-documentation-1/account-management/account-admin/customizations/templates/export-templates) fit into the process of exporting a report.
    """
    name = "List Export Templates"
    root = "/api/v2"
    path = f'/tenant/{tenantId}/export-templates'
    return request.get(base_url, headers, root+path, name)

def get_export_template(base_url, headers, tenantId, exportTemplateId):
    """
    Returns the file binary of the .docx file of the Export Template.
    """
    name = "Get Export Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/export-template/{exportTemplateId}'
    return request.get(base_url, headers, root+path, name)

def import_export_template(base_url, headers, tenantId, payload, name, type):
    """
    Imports a Microsoft Word .docx file with Jinja code into the platform as an export template.

    Query Parameters:
    name: Name of the file in the request body - example (plextrac-default-template.docx)
    type: String value "custom" - example (custom)
    """
    name = "Import Export Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/template/import?name={name}?type={type}'
    return request.post(base_url, headers, root+path, name, payload)

def delete_export_template(base_url, headers, tenantId, exportTemplateId):
    """
    No description in Postman
    """
    name = "Delete Export Template"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/template/{exportTemplateId}'
    return request.delete(base_url, headers, root+path, name)
