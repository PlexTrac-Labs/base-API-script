from utils import request_handler as request

def get_report_list(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    This request **retrieves a list of reports** for a tenant.

`pagination` is a required key while `sort` and `filters` are optional.

The `pagination.limit` must be one of \[5, 10, 25, 50, 100, 1000\]. The `pagination.offset` is the number of records to shift by, not the number of pages to shift by. i.e. offset 2, limit 10 gives you records 2-12 not 20-30

The following values can be used in the `filters.by` field:

- name
- reviewers (array of reviewer emails)
- operators(array of operator emails)
- clients (array of client IDs a report is under)
- status (array of report statuses)
    

The following values can be used in the `sort.by` field:

- name
- status
    

The following values can be used in the `sort.order` field:

- ASC
- DESC
    """
    name = "Get Report List"
    root = "/api/v2"
    path = f'/reports'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_delete_reports(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    No description in Postman
    """
    name = "Bulk Delete Reports"
    root = "/api/v2"
    path = f'/reports/bulk/delete'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_add_tags_to_report(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    No description in Postman
    """
    name = "Bulk Add Tags to Report"
    root = "/api/v2"
    path = f'/reports/bulk/tags'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_assign_reviewers_to_report(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    The reviewer email must match an existing PT user email.
    """
    name = "Bulk Assign Reviewers to Report"
    root = "/api/v2"
    path = f'/reports/bulk/reviewers'
    return request.post(base_url, headers, root+path, name, payload)

def bulk_adjust_status_of_report(base_url, headers, payload) -> PTWrapperLibraryResponse:
    """
    The reviewer email must match an existing PT user email.
    """
    name = "Bulk Adjust Status of Report"
    root = "/api/v2"
    path = f'/reports/bulk/status'
    return request.post(base_url, headers, root+path, name, payload)
