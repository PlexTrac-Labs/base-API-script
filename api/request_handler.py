import requests
import json

import utils.log_handler as logger
log = logger.log
import settings


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
def get(base_url, request_root, request_path, request_name, headers):
    try:
        response = requests.get(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            verify = settings.verify_ssl
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
def post(base_url, request_root, request_path, request_name, headers, payload):
    try:
        response = requests.post(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            json = payload,
            verify = settings.verify_ssl
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
def post_multipart(base_url, request_root, request_path, request_name, headers, multipart_form_data):
    try:
        response = requests.post(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            files = multipart_form_data,
            verify = settings.verify_ssl
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
def put(base_url, request_root, request_path, request_name, headers, payload):
    try:
        response = requests.put(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            json = payload,
            verify = settings.verify_ssl
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
def delete(base_url, request_root, request_path, request_name, headers):
    try:
        response = requests.delete(
            f'{base_url}{request_root}{request_path}',
            headers = headers,
            verify = settings.verify_ssl
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
