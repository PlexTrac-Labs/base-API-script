import api.request_handler as request

from api import *

#----------Report Endpoints----------
def list_reports(base_url, headers, client_id):
    api.client.list_reports(base_url, headers, client_id)

def get(base_url, headers, client_id, report_id):
    name = "Get Report"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}'
    return request.get(base_url, root, path, name, headers)

def create(base_url, headers, payload, client_id):
    name = "Create Report"
    root = "/api/v1"
    path = f'/client/{client_id}/report/create'
    return request.post(base_url, root, path, name, headers, payload)

def list_findings(base_url, headers, client_id, report_id):
    name = "List Report Findings"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaws'
    return request.get(base_url, root, path, name, headers)