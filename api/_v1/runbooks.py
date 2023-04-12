from utils import request_handler as request

def export_runbook(base_url, headers, runbookId):
    """
    No description in Postman
    """
    name = "Export Runbook"
    root = "/api/v1"
    path = f'/export/runbook/{runbookId}'
    return request.get(base_url, headers, root+path, name)

def import_runbook(base_url, headers):
    """
    No description in Postman
    """
    name = "Import Runbook"
    root = "/api/v1"
    path = f'/import/runbook'
    return request.post(base_url, headers, root+path, name)
