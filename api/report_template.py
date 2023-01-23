import api.request_handler as request

#----------Report Template Endpoints----------
def list(base_url, headers, tenant_id):
    name = "List Report Templates"
    root = "/api/v1"
    path = f'/tenant/{tenant_id}/report-templates'
    return request.get(base_url, root, path, name, headers)