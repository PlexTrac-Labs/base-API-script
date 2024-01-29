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

def search_tenant_tags(base_url, headers, tenantId, text, limit, offset):
    """
    This endpoint allows users to search for tags within a specific tenant.

#### Request Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| text | String | The text to search for within the tags |
| limit | Integer | The maximum number of tags to retrieve (optional) |
| offset | Integer | The number of tags to skip before starting to retrieve (optional) |

#### Response Fields

In the event of a successful request, the response will contain a 'count' array with the total number of matching tags and a 'tags' array with the list of tags. Each tag object will contain the following fields:

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | Unique identifier of the tag |
| name | String | Name of the tag |

In the event of an error, the response will not contain any specific error fields.

    Query Parameters:
    text: partial text of tag to search - example (example)
    limit: limit of results to return - example (20)
    offset: offset of results for pagination - example (0)
    """
    name = "Search Tenant Tags"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag/search?text={text}?limit={limit}?offset={offset}'
    return request.get(base_url, headers, root+path, name)

def find_tenant_tag(base_url, headers, tenantId, payload):
    """
    This endpoint allows developers to find a tag for a specific tenant.

#### Request Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| tenantId | String | The unique identifier of the tenant |
|  |  |  |

#### Response Fields

In the event of a successful request, the response will contain an object with the following fields:

| Parameter | Type | Description |
| --- | --- | --- |
| id | String | The unique identifier of the tag |
| name | String | The name of the tag |

In the event of an error, the response will contain an 'error' object with a 'message' field describing the error.
    """
    name = "Find Tenant Tag"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/tag/find'
    return request.post(base_url, headers, root+path, name, payload)
