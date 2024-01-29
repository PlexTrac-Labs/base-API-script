from utils import request_handler as request

def clientasset(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "clientAsset"
    root = ""
    path = "/graphql"
    return request.post(base_url, headers, root+path, name, payload)
