from utils import request_handler as request

def import_writeups_to_repository(base_url, headers, source, payload) -> PTWrapperLibraryResponse:
    """
    This request **imports a repository** and to the **WriteupsDB** module.

The source should be .csv, and the file should be the path to the csv file.
    """
    name = "Import Writeups to Repository"
    root = "/api/v2"
    path = f'/writeups/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_copy_writeups(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request **copies writeups from a repository** in the **WriteupsDB** module.
    """
    name = "Bulk Copy Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/copy'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_move_writeups(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request **moves a writeup to another repository** in the **WriteupsDB** module.
    """
    name = "Bulk Move Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/move'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_delete_writeups(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request **deletes a writeup** in the **WriteupsDB** module.
    """
    name = "Bulk Delete Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/delete'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_add_tags_to_writeups(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request **adds tags to a writeup** in the **WriteupsDB** module.
    """
    name = "Bulk Add Tags to Writeups"
    root = "/api/v2"
    path = f'/writeups/bulk/tags'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_add_writeups_to_report(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request adds **a writeup** in the **WriteupsDB** module to an existing report.
    """
    name = "Bulk Add Writeups to Report"
    root = "/api/v2"
    path = f'/writeups/bulk/addToReport'
    return request.post(base_url, headers, root+path, name, payload)

def add_writeups_to_repository(base_url, headers, repositoryId, payload) -> PTWrapperLibraryResponse:
    """
    This request **moves a writeup** in the **WriteupsDB** module to different repository.
    """
    name = "Add Writeups to Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/addWriteups'
    return request.post(base_url, headers, root+path, name, payload)

def remove_writeups_from_repository(base_url, headers, repositoryId, payload) -> PTWrapperLibraryResponse:
    """
    This request removes **a writeup from a specific repository** in the **WriteupsDB** module.
    """
    name = "Remove Writeups from Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/removeWriteup'
    return request.post(base_url, headers, root+path, name, payload)

def get_writeups_from_repository(base_url, headers, repositoryId, payload) -> PTWrapperLibraryResponse:
    """
    This request **retrieves all writeups from a specific repository** in the **WriteupsD**B module.
    """
    name = "Get Writeups from Repository"
    root = "/api/v2"
    path = f'/repositories/{repositoryId}/getWriteups'
    return request.post(base_url, headers, root+path, name, payload)
