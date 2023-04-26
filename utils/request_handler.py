import requests
import requests.packages
from typing import Dict
from json import JSONDecodeError
import time

import settings
import utils.log_handler as logger
log = logger.log

from api.exceptions import *


class PTWrapperLibraryResponse():
    def __init__(self, response: requests.Response, status_code: int, message: str = '', json: dict = None):
        self.response = response
        self.status_code = int(status_code)
        self.message = str(message)

        self.has_json_response = True if json else False
        self.json = json if json else {}

if not settings.verify_ssl:
    # noinspection PyUnresolvedReferences
    requests.packages.urllib3.disable_warnings()

def _do(http_method: str, base_url: str, headers: dict, endpoint: str, name: str, data: Dict = None, files = None) -> PTWrapperLibraryResponse:
    """
    :param http_method: HTTP method, GET, POST, PUT, DELETE
    :type http_method: str
    :param base_url: URL to PT instance including protocol (ex. https://example.plextrac.com)
    :type base_url: str
    :param headers: dictionary of request headers
    :type headers: dict
    :param endpoint: endpoint will be concatenated to `base_url` as the URL to send the request to
    :type endpoint: str
    :param name: name of API endpoint, mentioned during exceptions
    :type name: str
    :param data: request payload, defaults to None
    :type data: Dict, optional
    :param files: file data send in a multipart form request, defaults to None
    :type files: _type_, optional
    :raises PTWrapperLibraryException: general request failure
    :raises PTWrapperLibraryJSONResponse: request doesn't return JSON data
    :raises PTWrapperLibraryFailed: non 200 response
    :return: custom wrapper for Python requests.Response object
    :rtype: PTWrapperLibraryResponse
    """      
    full_url = base_url + endpoint
    log_line_pre = f"method={http_method}, url={full_url}"
    log_line_post = ', '.join((log_line_pre, "success={}, status_code={}, message={}"))
    
    retries = 0
    while retries <= settings.retries:
        # Log HTTP params and perform an HTTP request, catching and re-raising any exceptions
        try:
            log.debug(log_line_pre)
            response = requests.request(method=http_method, url=full_url, verify=settings.verify_ssl, headers=headers, json=data, files=files)
        except requests.exceptions.RequestException as e:
            if retries < settings.retries:
                retries += 1
                log.exception(f'Request failed - {name}. Retrying... ({retries}/{settings.retries})\nException: {str(e)}')
                time.sleep(5)
                continue # if this part doesn't succeed you can't continue. prevents incrementing `retries` more than once in a single attempt
            else:
                raise PTWrapperLibraryException(f'Request failed - {name}') from e
        # Deserialize JSON output to Python object, or return failed PTWrapperLibraryResponse on exception
        try:
            data_out = response.json()
        except (ValueError, JSONDecodeError) as e:
            if retries < settings.retries:
                retries += 1
                log.exception(log_line_post.format(False, None, e))
                time.sleep(5)
                continue # if this part doesn't succeed you can't continue. prevents incrementing `retries` more than once in a single attempt
            else:
                raise PTWrapperLibraryJSONResponse(f'Bad JSON response - {name}') from e
        # If status_code in 200-299 range, return success PTWrapperLibraryResponse with data, otherwise raise exception
        is_success = 299 >= response.status_code >= 200
        log_line = log_line_post.format(is_success, response.status_code, response.reason)
        if is_success:
            log.debug(log_line)
            return PTWrapperLibraryResponse(response, response.status_code, message=response.reason, json=data_out)
        if retries < settings.retries:
            retries += 1
            log.exception(log_line)
            time.sleep(5)
            continue # if this part doesn't succeed you can't continue. prevents incrementing `retries` more than once in a single attempt
        else:
            log.exception(f'{log_line}, pt_message={data_out.get("message")}')
            raise PTWrapperLibraryFailed(f'{name} - {response.status_code}: {response.reason}')
    
def get(base_url: str, headers: dict, endpoint: str, name: str) -> PTWrapperLibraryResponse:
    """
    GET request wrapper

    :param base_url: URL to PT instance including protocol (ex. https://example.plextrac.com)
    :type base_url: str
    :param headers: dictionary of request headers
    :type headers: dict
    :param endpoint: endpoint will be concatenated to `base_url` as the URL to send the request to
    :type endpoint: str
    :param name: name of API endpoint, mentioned during exceptions
    :type name: str
    :return: custom wrapper for Python requests.Response object
    :rtype: PTWrapperLibraryResponse
    """    
    return _do(http_method='GET', base_url=base_url, headers=headers, endpoint=endpoint, name=name)

# sending image file in POST Upload Image to Tenant requires the following files data
# {
#     'setScope': (None, '["tenant_admin_0","tenant_std_user_0","tenant_analyst_0"]', "text/plain"),
#     'file': file
# }
# where file is img in `with open(f'{image_path}{image_file_name}.{ext}', "rb") as img:`
def post(base_url: str, headers: dict, endpoint: str, name: str, data: Dict = None, files = None) -> PTWrapperLibraryResponse:
    """
    POST request wrapper

    :param base_url: URL to PT instance including protocol (ex. https://example.plextrac.com)
    :type base_url: str
    :param headers: dictionary of request headers
    :type headers: dict
    :param endpoint: endpoint will be concatenated to `base_url` as the URL to send the request to
    :type endpoint: str
    :param name: name of API endpoint, mentioned during exceptions
    :type name: str
    :param data: request payload, defaults to None
    :type data: Dict, optional
    :param files: file data send in a multipart form request, defaults to None
    :type files: _type_, optional
    :return: custom wrapper for Python requests.Response object
    :rtype: PTWrapperLibraryResponse
    """  
    return _do(http_method='POST', base_url=base_url, headers=headers, endpoint=endpoint, name=name, data=data, files=files)
    
def put(base_url: str, headers: dict, endpoint: str, name: str, data: Dict = None) -> PTWrapperLibraryResponse:
    """
    PUT request wrapper

    :param base_url: URL to PT instance including protocol (ex. https://example.plextrac.com)
    :type base_url: str
    :param headers: dictionary of request headers
    :type headers: dict
    :param endpoint: endpoint will be concatenated to `base_url` as the URL to send the request to
    :type endpoint: str
    :param name: name of API endpoint, mentioned during exceptions
    :type name: str
    :param data: request payload, defaults to None
    :type data: Dict, optional
    :return: custom wrapper for Python requests.Response object
    :rtype: PTWrapperLibraryResponse
    """  
    return _do(http_method='PUT', base_url=base_url, headers=headers, endpoint=endpoint, name=name, data=data)
    
def delete(base_url: str, headers: dict, endpoint: str, name: str, data: Dict = None) -> PTWrapperLibraryResponse:
    """
    DELETE request wrapper

    :param base_url: URL to PT instance including protocol (ex. https://example.plextrac.com)
    :type base_url: str
    :param headers: dictionary of request headers
    :type headers: dict
    :param endpoint: endpoint will be concatenated to `base_url` as the URL to send the request to
    :type endpoint: str
    :param name: name of API endpoint, mentioned during exceptions
    :type name: str
    :param data: request payload, defaults to None
    :type data: Dict, optional
    :return: custom wrapper for Python requests.Response object
    :rtype: PTWrapperLibraryResponse
    """  
    return _do(http_method='DELETE', base_url=base_url, headers=headers, endpoint=endpoint, name=name, data=data)