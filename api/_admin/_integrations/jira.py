from utils import request_handler as request

def list_jira_projects(base_url, headers):
    """
    This request **retrieves a list of Jira projects** that are used to associate a finding ticket to**.**
    """
    name = "List Jira Projects"
    root = "/api/v1"
    path = f'/jira/projects'
    return request.get(base_url, headers, root+path, name)

def create_and_link_jira_ticket_to_finding(base_url, headers, clientId, reportId, findingId, payload):
    """
    This request **creates a finding for a specific report and creates a Jira ticket**, if that integration is configured.
    """
    name = "Create and Link Jira Ticket to Finding"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/flaw/{findingId}/createAndLinkJiraTicket'
    return request.post(base_url, headers, root+path, name, payload)
