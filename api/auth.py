import api.request_handler as request

# utility and authentication endpoints
def root(base_url, headers):
    name = "Root"
    root = "/api/v1"
    path = "/"
    return request.get(base_url, root, path, name, headers)

def authenticate(base_url, headers, payload):
    name = "Authenticate"
    root = "/api/v1"
    path = "/authenticate"
    return request.post(base_url, root, path, name, headers, payload)

def mfa_authenticate(base_url, headers, payload):
    name = "MFA Authenticate"
    root = "/api/v1"
    path = "/authenticate/mfa"
    return request.post(base_url, root, path, name, headers, payload)