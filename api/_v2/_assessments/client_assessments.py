from utils import request_handler as request

def list_tenant_assessments(base_url, headers, tenantId, limit, offset, order, clientId, sort, filter) -> PTWrapperLibraryResponse:
    """
    This request **retrieves a list of assessments** for a specific tenant with the ability to sort and filter results.

    Query Parameters:
    limit: (number, default: 10) pagination limit - example (10)
    offset: (number, default: 0) pagination offset - example (0)
    order: (string, default: ascend) sort by date (ascend/descend) - example (ascend)
    clientId: filter by client id - example ()
    sort: (string, default: ALL_ASCEND)
ALL_ASCEND: completed first,
ALL_DESCEND: in progress first,
IN_PROGRESS: only in progress
COMPLETED: only completed - example (ALL_DESCEND)
    filter: (string) filter results by assessment title - example ()
    """
    name = "List Tenant Assessments"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/assessments?limit={limit}?offset={offset}?order={order}?clientId={clientId}?sort={sort}?filter={filter}'
    return request.get(base_url, headers, root+path, name)

def list_client_assessments(base_url, headers, tenantId, clientId, offset, limit, sort, order, filter) -> PTWrapperLibraryResponse:
    """
    No description in Postman

    Query Parameters:
    offset: (number, default: 0) pagination offset - example (0)
    limit: (number, default: 10) pagination limit - example (10)
    sort: (number, default: 0) 0 - IN_PROGRESS,
1 - COMPLETED,
2 - COMPLETED_ASC - all with completed at top,
3 - COMPLETED_DESC - all with completed at bottom - example (0)
    order: (string, default: ascend) ascend, most recent last, descend - most recent first - example (ascend)
    filter: (string) assessment title filter - example (None)
    """
    name = "List Client Assessments"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments?offset={offset}?limit={limit}?sort={sort}?order={order}?filter={filter}'
    return request.get(base_url, headers, root+path, name)

def get_client_assessment(base_url, headers, tenantId, clientId, assessmentId) -> PTWrapperLibraryResponse:
    """
    This request **returns the data for a specific assessment** started for **a specific client**.

You can determine if the assessment is **In Progress** or **Completed** with the addition of the `completed_at` field in the response.

*   If this field is included in the response, the assessment was **completed** at the time value given.
*   If the field is not included in the response, the assessment is **In Progress**.
    """
    name = "Get Client Assessment"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}'
    return request.get(base_url, headers, root+path, name)

def get_assessment_questions(base_url, headers, tenantId, clientId, assessmentId, offset, limit, order) -> PTWrapperLibraryResponse:
    """
    This request **retrieves questions for a specific assessment** for **a specific client** with the ability to sort and filter results.

    Query Parameters:
    offset: (number, default: 0) pagination offset - example (0)
    limit: (number, default: 10) pagination limit - example (3)
    order: (string, default: ascend) order by question id, ascending/descending - example (ascend)
    """
    name = "Get Assessment Questions"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/questions?offset={offset}?limit={limit}?order={order}'
    return request.get(base_url, headers, root+path, name)

def get_assessment_answers(base_url, headers, tenantId, clientId, assessmentId, limit, offset, order) -> PTWrapperLibraryResponse:
    """
    This request **retrieves answers for a specific assessment** for **a specific client** with the ability to sort and filter results.

    Query Parameters:
    limit: (number, default: 10) pagination limit - example (3)
    offset: (number, default: 0) pagination offset - example (0)
    order: (string, default: ascend) qid ordering, ascend/descend - example (ascend)
    """
    name = "Get Assessment Answers"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers?limit={limit}?offset={offset}?order={order}'
    return request.get(base_url, headers, root+path, name)

def update_assessment_answers(base_url, headers, tenantId, clientId, assessmentId, payload) -> PTWrapperLibraryResponse:
    """
    This request **updates answers** for an assessment.
    """
    name = "Update Assessment Answers"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers'
    return request.put(base_url, headers, root+path, name, payload)

def get_assessment_reviewers(base_url, headers, tenantId, clientId, assessmentId) -> PTWrapperLibraryResponse:
    """
    This request **retrieves a list of reviewers** for a an assessment.
    """
    name = "Get Assessment Reviewers"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers'
    return request.get(base_url, headers, root+path, name)

def copy_asessment_questionnaire(base_url, headers, tenantId, clientId, assessmentId, payload) -> PTWrapperLibraryResponse:
    """
    This request **creates a new assessment** from a previously completed assessment, copying over questions and answers.
    """
    name = "Copy Asessment Questionnaire"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy'
    return request.post(base_url, headers, root+path, name, payload)
