import api.request_handler as request

#----------Client Endpoints----------
def list(base_url, headers, filter_tag):
    name = "List Clients"
    root = "/api/v2"
    path = "/clients"
    payload = {
        "pagination": {
            "offset": 0,
            "limit": 100
        },
        "filters": [{ "by": "tags", "value": [filter_tag] }]
    }
    return request.post(base_url, root, path, name, headers, payload)

def get(base_url, headers, client_id):
    name = "Get Client"
    root = "/api/v1"
    path = f'/client/{client_id}'
    return request.get(base_url, root, path, name, headers)

def create(base_url, headers, payload):
    name = "Create Client"
    root = "/api/v1"
    path = f'/client/create'
    return request.post(base_url, root, path, name, headers, payload)

def list_reports(base_url, headers, client_id):
    name = "List Reports"
    root = "/api/v2"
    path = f'/reports'
    payload = {
        "pagination": {
            "offset": 0,
            "limit": 100
        },
        "filters": [{ "by": "clients", "value": [client_id] }]
    }
    return request.post(base_url, root, path, name, headers, payload)

def list_assets(base_url, headers, client_id):
    name = "Get Asset List"
    root = "/api/v1"
    path = f'/client/{client_id}/assets'
    return request.get(base_url, root, path, name, headers)