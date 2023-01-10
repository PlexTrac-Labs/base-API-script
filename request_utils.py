import requests
import json

import settings
log = settings.log

# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
# TODO - move to config
verify_ssl = True

# call if the api call fails, generally 500 codes
def err_requests_general(request, type, path, e):
    log.error(f'Could not complete {type} \'{request}\' on \'{path}\' endpoint. Exception: {e}')

# call when the api call returns a non success, generally 400 codes
def err_non_200_response(request, status, reason):
    log.error(f'\'{request}\' request failed with status: {status} - {reason}')

# call when the api call doesn't return a valid json response, if a json response was expected
def err_invalid_json_response(request, e):
    log.error(f'Malformed \'{request}\' API response. Exception: {e}')

# call when the api call is missing a specific field, when that field is expected
def err_missing_required_response_field(request, field):
    log.error(f'Received empty \'{field}\' value from server')


# general GET request with error messages inserted
# - assumes GET requests will not have a body
def request_get(base_url, request_root, request_path, request_name, headers):
    try:
        response = requests.get(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            verify = verify_ssl
        )

        try:
            response_json = json.loads(response.text)

            if response.status_code != 200:
                err_non_200_response(request_name, response.status_code, response.reason)
                log.warning(f'Plextrac message: {response_json.get("message")}')
        except Exception as e:
            err_invalid_json_response(request_name, e)
            return response

        return response_json
        
    except Exception as e:
        err_requests_general(request_name, "GET", request_path, e)
        exit()


# general POST request with error messages inserted
def request_post(base_url, request_root, request_path, request_name, headers, payload):
    try:
        response = requests.post(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            json = payload,
            verify = verify_ssl
        )

        try:
            response_json = json.loads(response.text)

            if response.status_code != 200:
                err_non_200_response(request_name, response.status_code, response.reason)
                log.warning(f'Plextrac message: {response_json.get("message")}')
        except Exception as e:
            err_invalid_json_response(request_name, e)
            return response

        return response_json
        
    except Exception as e:
        err_requests_general(request_name, "POST", request_path, e)
        exit()


# POST request for multipart form-data with error messages inserted
def request_post_multipart(base_url, request_root, request_path, request_name, headers, multipart_form_data):
    try:
        response = requests.post(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            files = multipart_form_data,
            verify = verify_ssl
        )

        try:
            response_json = json.loads(response.text)

            if response.status_code != 200:
                err_non_200_response(request_name, response.status_code, response.reason)
                log.warning(f'Plextrac message: {response_json.get("message")}')
        except Exception as e:
            err_invalid_json_response(request_name, e)
            return response

        return response_json
        
    except Exception as e:
        err_requests_general(request_name, "POST", request_path, e)
        exit()


# general PUT request with error messages inserted
def request_put(base_url, request_root, request_path, request_name, headers, payload):
    try:
        response = requests.put(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            json = payload,
            verify = verify_ssl
        )

        try:
            response_json = json.loads(response.text)

            if response.status_code != 200:
                err_non_200_response(request_name, response.status_code, response.reason)
                log.warning(f'Plextrac message: {response_json.get("message")}')
        except Exception as e:
            err_invalid_json_response(request_name, e)
            return response

        return response_json
        
    except Exception as e:
        err_requests_general(request_name, "PUT", request_path, e)
        exit()
        

# general DELETE request with error messages inserted
# - assumes DELETE requests will not have a body
def request_delete(base_url, request_root, request_path, request_name, headers):
    try:
        response = requests.delete(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            verify = verify_ssl
        )

        try:
            response_json = json.loads(response.text)

            if response.status_code != 200:
                err_non_200_response(request_name, response.status_code, response.reason)
                log.warning(f'Plextrac message: {response_json.get("message")}')
        except Exception as e:
            err_invalid_json_response(request_name, e)
            return response

        return response_json
        
    except Exception as e:
        err_requests_general(request_name, "POST", request_path, e)
        exit()


# list of endpoints - keeps like data together, static place for root and path info
def request_root(base_url, headers):
    name = "Root"
    root = "/api/v1"
    path = "/"
    return request_get(base_url, root, path, name, headers)

def request_authenticate(base_url, headers, payload):
    name = "Authenticate"
    root = "/api/v1"
    path = "/authenticate"
    return request_post(base_url, root, path, name, headers, payload)

def request_mfa_authenticate(base_url, headers, payload):
    name = "MFA Authenticate"
    root = "/api/v1"
    path = "/authenticate/mfa"
    return request_post(base_url, root, path, name, headers, payload)

#----------Client Endpoints----------
def request_list_clients(base_url, headers, filter_tag):
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
    return request_post(base_url, root, path, name, headers, payload)

def request_get_client(base_url, headers, client_id):
    name = "Get Client"
    root = "/api/v1"
    path = f'/client/{client_id}'
    return request_get(base_url, root, path, name, headers)

def request_create_client(base_url, headers, payload):
    name = "Create Client"
    root = "/api/v1"
    path = f'/client/create'
    return request_post(base_url, root, path, name, headers, payload)

#----------Report Endpoints----------
def request_list_reports(base_url, headers, client_id):
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
    return request_post(base_url, root, path, name, headers, payload)

def request_get_report(base_url, headers, client_id, report_id):
    name = "Get Report"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}'
    return request_get(base_url, root, path, name, headers)

def request_create_report(base_url, headers, payload, client_id):
    name = "Create Report"
    root = "/api/v1"
    path = f'/client/{client_id}/report/create'
    return request_post(base_url, root, path, name, headers, payload)

#----------Finding Endpoints----------
def request_list_report_findings(base_url, headers, client_id, report_id):
    name = "List Report Findings"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaws'
    return request_get(base_url, root, path, name, headers)

def request_get_finding(base_url, headers, client_id, report_id, finding_id):
    name = "Get Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request_get(base_url, root, path, name, headers)

def request_create_finding(base_url, headers, payload, client_id, report_id):
    name = "Create Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/create'
    return request_post(base_url, root, path, name, headers, payload)

def request_update_finding(base_url, headers, payload, client_id, report_id, finding_id):
    name = "Update Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request_put(base_url, root, path, name, headers, payload)

def request_delete_finding(base_url, headers, client_id, report_id, finding_id):
    name = "Delete Finding"
    root = "/api/v1"
    path = f'/client/{client_id}/report/{report_id}/flaw/{finding_id}'
    return request_delete(base_url, root, path, name, headers)

#----------Asset Endpoints----------
def request_list_assets(base_url, headers, client_id):
    name = "Get Asset List"
    root = "/api/v1"
    path = f'/client/{client_id}/assets'
    return request_get(base_url, root, path, name, headers)

def request_get_asset(base_url, headers, client_id, asset_id):
    name = "Get Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request_get(base_url, root, path, name, headers)

def request_create_asset(base_url, headers, payload, client_id):
    name = "Create Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/0'
    return request_put(base_url, root, path, name, headers, payload)

def request_update_asset(base_url, headers, payload, client_id, asset_id):
    name = "Update Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request_put(base_url, root, path, name, headers, payload)

def request_delete_asset(base_url, headers, client_id, asset_id):
    name = "Delete Asset"
    root = "/api/v1"
    path = f'/client/{client_id}/asset/{asset_id}'
    return request_delete(base_url, root, path, name, headers)

#----------Report Template Endpoints----------
def request_list_report_templates(base_url, headers, tenant_id):
    name = "List Report Templates"
    root = "/api/v1"
    path = f'/tenant/{tenant_id}/report-templates'
    return request_get(base_url, root, path, name, headers)

#----------Findings Template Endpoints----------
def request_list_findings_templates(base_url, headers):
    name = "List Findings Templates"
    root = "/api/v1"
    path = f'/field-templates'
    return request_get(base_url, root, path, name, headers)