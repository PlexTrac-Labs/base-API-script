from utils import request_handler as request

def list_tenant_tags(base_url, headers, tenantId, limit, offset):
    """
    This request retrieves **a list of all tags for a tenant** with filter options.

    Query Parameters:
    limit: No description in Postman - example (10)
    offset: No description in Postman - example (0)
    """
    name = "List Tenant Tags"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag?limit={limit}?offset={offset}'
    return request.get(base_url, headers, root+path, name)

def create_tenant_tag(base_url, headers, tenantId, payload):
    """
    This request creates **a new tag for a tenant.** A created tag will be listed on the tag dropdown that appears when typing to add a tag anywhere in the platform. This functionality is found in the platform under Account Admin > Tag Settings > Create Tag

The `scope` should be `"tenant"`

The `ownerId` is the `tenantId`

This endpoint returns an empty array `[]` when successful
    """
    name = "Create Tenant Tag"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag'
    return request.post(base_url, headers, root+path, name, payload)

def delete_tenant_tag(base_url, headers, tenantId, tagId):
    """
    This request creates **a new tag for a tenant.** This functionality is found in the platform under Account Admin > Tag Settings > Actions > Delete

The `tagId` should be a string with the format `tag_[scope]_[ownerId]_[name]` i.e. `tag_tenant_0_new_test_tag`
    """
    name = "Delete Tenant Tag"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag/{tagId}'
    return request.delete(base_url, headers, root+path, name)
