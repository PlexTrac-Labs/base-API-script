from utils import request_handler as request

def get_report_list(base_url, headers, payload):
    """
    This request **retrieves a list of reports** for a tenant.

`pagination` is a required key while `sort` and `filters` are optional.

The `pagination.limit` must be one of \[5, 10, 25, 50, 100\]. The `pagination.offset` is the number of records to shift by, not the number of pages to shift by. i.e. offset 2, limit 10 gives you records 2-12 not 20-30

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
