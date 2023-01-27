import api.request_handler as request

#----------Findings Template Endpoints----------
def list(base_url, headers):
    name = "List Findings Templates"
    root = "/api/v1"
    path = f'/field-templates'
    return request.get(base_url, root, path, name, headers)