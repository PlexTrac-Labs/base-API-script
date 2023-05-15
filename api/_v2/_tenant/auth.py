from utils import request_handler as request

def get_available_authentication_providers(base_url, headers):
    """
    Return a list of supported authentication providers
    """
    name = "Get Available Authentication Providers"
    root = "/api/v2"
    path = f'/authenticate/providers'
    return request.get(base_url, headers, root+path, name)

def get_tenant_provider_authentication_configuration(base_url, headers, tenantId, authProvider):
    """
    Admin only route, update authentication provider configuration
    """
    name = "Get Tenant Provider Authentication Configuration"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/providers/{authProvider}'
    return request.get(base_url, headers, root+path, name)

def update_tenant_authentication_provider_configuration(base_url, headers, tenantId, authProvider, payload):
    """
    Update configuration for tenant authentication providers (Okta, Azure AD, Google) (Admin only)
    """
    name = "Update Tenant Authentication Provider Configuration"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/providers/{authProvider}'
    return request.post(base_url, headers, root+path, name, payload)

def update_tenant_user_authentication_method(base_url, headers, tenantId, userId, payload):
    """
    Update the authentication method a tenant user is authorized to log in with (admin only)
    """
    name = "Update Tenant User Authentication Method"
    root = "/api/v2"
    path = f'/authenticate/tenants/{tenantId}/users/{userId}/configuration'
    return request.put(base_url, headers, root+path, name, payload)

def get_saml_provider(base_url, headers, tenantId, authProvider):
    """
    Endpoint for getting a single saml provider configuration, validate: {
        params: {
            tenantId: Joi.number()
                .integer()
                .required(),
            providerName: Joi.string()
                .required(),
        },
        failAction,
    },
    auth: {
        scope: ['global_admin', 'tenant_admin_{params.tenantId}'],
    },
    """
    name = "Get Saml Provider"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/saml/{authProvider}'
    return request.get(base_url, headers, root+path, name)

def upsert_saml_configuration(base_url, headers, tenantId, authProvider):
    """
    Endpoint for updating and creating saml providers for a tenant.

params: {
            tenantId: Joi.number()
                .integer()
                .required(),
            providerName: Joi.string()
                .required(),
        },
        payload: {
            enabled: Joi.boolean().required(),
            providerName: Joi.string().required(),
            issuer: Joi.string().required(),
            cert: Joi.string().required(),
            idpSSOUrl: Joi.string().required(),
        }
    """
    name = "Upsert Saml Configuration"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/saml/{authProvider}'
    return request.post(base_url, headers, root+path, name)
