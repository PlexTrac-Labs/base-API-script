from utils import request_handler as request

def bulk_create_and_link_jira_tickets_to_findings(base_url, headers, clientId, reportId, payload):
    """
    This request **retrieves findings from a specific report and creates Jira tickets**, if that integration is configured.
    """
    name = "Bulk Create and Link Jira Tickets to Findings"
    root = "/api/v2"
    path = f'/client/{clientId}/report/{reportId}/findings/createJiraTickets'
    return request.post(base_url, headers, root+path, name, payload)
