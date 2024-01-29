from utils import request_handler as request

def get_upload_by_name(base_url, headers):
    """
    This endpoint returns an inline image that was pasted in a rich text CKE field in the platform.

**Authentication:**

This endpoint has a non standard authentication workflow that is based solely on cookies. When authenticating to Plextrac with the normal authentication endpoint, there is a `cookie` and `token` value returned in the response. For the **Get Upload by Name** endpoint's authentication you need to send the `cookie` value as a cookie in the request. The `token` value, normally sent as the JWT Authorization header, should not be sent or you will get a 401 error.

Cookies consists of a name, value, and additional attributes. The cookie used for authentication on this endpoint has the follwoing:

**name**: "token"

**value**: `cookie` value from authentication endpoint response
    """
    name = "Get Upload by Name"
    root = "/api/v1"
    path = f'/uploads/9bee9f28-7e25-4b4f-8b64-b520fc3c0b7c.png'
    return request.get(base_url, headers, root+path, name)

def upload_image_to_tenant(base_url, headers, payload):
    """
    No description in Postman
    """
    name = "Upload Image to Tenant"
    root = "/api/v1"
    path = f'/uploads'
    return request.post(base_url, headers, root+path, name, payload)
