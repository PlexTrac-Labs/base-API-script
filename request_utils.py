import requests
import json

# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True

# call if the api call fails, generally 500 codes
def err_requests_general(request, type, path, e):
    print(f'Err: Could not complete {type} \'{request}\' on \'{path}\' endpoint. Exception: {e}')

# call when the api call returns a non success, generally 400 codes
def err_non_200_response(request, status, reason):
    print(f'Err: \'{request}\' request failed with status: {status} - {reason}')

# call when the api call doesn't return a valid json response, if a json response was expected
def err_invalid_json_response(request, e):
    print(f'Err: Malformed \'{request}\' API response. Exception: {e}')

# call when the api call is missing a specific field, when that field is expected
def err_missing_required_response_field(request, field):
    print(f'Err: Received empty \'{field}\' value from server')


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
                print(f'Plextrac message: {response_json.get("message")}')
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
                print(f'Plextrac message: {response_json.get("message")}')
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
                print(f'Plextrac message: {response_json.get("message")}')
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
                print(f'Plextrac message: {response_json.get("message")}')
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
