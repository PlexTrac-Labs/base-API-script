from utils import request_handler as request

def generate_qr_code(base_url, headers):
    """
    This request **generates a QR code link** that can be used to set up multi-factor authorization (MFA).

NOTE: This action will override previous MFA setup.
    """
    name = "Generate QR code"
    root = "/api/v2"
    path = f'/user/mfa/qr'
    return request.get(base_url, headers, root+path, name)

def activate_mfa(base_url, headers, payload):
    """
    This request **activates a QR code** that is used to set up multi-factor authorization (MFA) by including the six-digit MFA code provided by the third-party authorization tool as a variable in the body.
    """
    name = "Activate MFA"
    root = "/api/v2"
    path = f'/user/mfa/qr/activate'
    return request.post(base_url, headers, root+path, name, payload)
