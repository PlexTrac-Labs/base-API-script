import api.request_handler as request

from api import *

#----------Asset Endpoints----------
def list_assets(base_url, headers, client_id):
    api.client.list_assets(base_url, headers, client_id)

def get(base_url, headers, client_id, asset_id):
    name = "Get Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request.get(base_url, root, path, name, headers)

def create(base_url, headers, payload, client_id):
    name = "Create Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/0'
    return request.put(base_url, root, path, name, headers, payload)

def update(base_url, headers, payload, client_id, asset_id):
    name = "Update Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request.put(base_url, root, path, name, headers, payload)

def delete(base_url, headers, client_id, asset_id):
    name = "Delete Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request.delete(base_url, root, path, name, headers)