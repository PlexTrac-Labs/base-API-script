from utils import request_handler as request

def list_instances(base_url, headers, page_size=10, page_number=1):
    """
    This request **retrieves a list of instances for a specific report**.
    """
    name = "List Instances"
    root = "/api/experimental"
    path = f'/finding-instances?page[current]={page_number}&page[size]={page_size}'
    return request.get(base_url, headers, root+path, name)

def get_instance(base_url, headers, cuid):
    """
    This request **retrieves a specific instance** based on CUID.
    """
    name = "Get Instance"
    root = "/api/experimental"
    path = f'/finding-instances/{cuid}'
    return request.get(base_url, headers, root+path, name)

def patch_instance(base_url, headers, cuid, payload):
    """
    This request **patches a specific instance** based on CUID.
    
    The following values are tested to be used in the payload:
        {
            "severity" : 1,
            "isSeverityCalculated" : false,
            "status" : "In Process",
            "substatusCuid" : null,
            "description" : "<p>description</p>",
            "scores" : {},
            "selectedScore" : null,
            "assignedToUserCuid" : null,
            "tags" : [],
            "cveStrings" : null,
            "cweStrings" : [],
            "recommendations" : "",
            "references" : "",
            "customFields" : [],
            "evidence" : [],
            "codeSamples" : [],
            "exhibits" : []
        }
    """
    name = "Patch Instance"
    root = "/api/experimental"
    path = f'/finding-instances/{cuid}'
    return request.patch(base_url, headers, root+path, name, payload)
