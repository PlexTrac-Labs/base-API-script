import api.request_handler as request

from api import *

#----------Finding Endpoints----------
def list_findings(base_url, headers, client_id, report_id):
    api.report.list_findings(base_url, headers, client_id, report_id)

def get(base_url, headers, client_id, report_id, finding_id):
    name = "Get Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request.get(base_url, root, path, name, headers)

def create(base_url, headers, payload, client_id, report_id):
    name = "Create Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/create'
    return request.post(base_url, root, path, name, headers, payload)

def update(base_url, headers, payload, client_id, report_id, finding_id):
    name = "Update Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request.put(base_url, root, path, name, headers, payload)

def delete(base_url, headers, client_id, report_id, finding_id):
    name = "Delete Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request.delete(base_url, root, path, name, headers)