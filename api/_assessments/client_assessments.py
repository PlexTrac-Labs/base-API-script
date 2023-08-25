from utils import request_handler as request

def list_tenant_assessments(base_url, headers, tenantId, limit, offset, order, clientId, sort, filter):
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

def list_client_assessments(base_url, headers, tenantId, clientId):
    """
    This request retrieves a list of **all** assessments for **a specific client** within a tenant.

The `instanceUrl` , `tenantId` and `clientId` is needed to execute the call.

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| client_name | name of client | Karbo Industries |
| tenant_id | ID of tenant | 0 |
| assess_ID | assessment ID | 3098 |
| questionniare_id | ID of questionnaire | 1345 |
| assessment_title | title of assessment | CIS Control 12: Boundary Defense |
| doc_type | document type | assessment |
| assessment_date | date assessment was created | 1652733751471 |
| saved_at | date assessment was last saved | 1652733751471 |
| last_updated_by | user who saved assessment | 0 |
| has_reviewers | identifies if assessment has reviewers or not | false |
| reviewers | if assessment has reviewers, they will be listed here | \[\] |
| all_approved | if applicable, identifies if assessment has been approved by all reviewers | false |
    """
    name = "List Client Assessments"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessments'
    return request.get(base_url, headers, root+path, name)

def list_client_assessments_filtered(base_url, headers, tenantId, clientId, offset, limit, sort, order, filter):
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
    name = "List Client Assessments (Filtered)"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments?offset={offset}?limit={limit}?sort={sort}?order={order}?filter={filter}'
    return request.get(base_url, headers, root+path, name)

def get_client_assessment_with_questions_and_answers(base_url, headers, tenantId, clientId, assessmentId):
    """
    This request retrieves a list of **a specific** assessment for **a specific client** within a tenant.

The `instanceUrl` , `tenantId` , `clientId`, and `assessmentID` is needed to execute the call.
    """
    name = "Get Client Assessment (with questions and answers)"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'
    return request.get(base_url, headers, root+path, name)

def get_client_assessment(base_url, headers, tenantId, clientId, assessmentId):
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

def get_assessment_questions(base_url, headers, tenantId, clientId, assessmentId, offset, limit, order):
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

def get_assessment_answers(base_url, headers, tenantId, clientId, assessmentId, limit, offset, order):
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

def update_assessment_answers(base_url, headers, tenantId, clientId, assessmentId, payload):
    """
    This request **updates answers** for an assessment.
    """
    name = "Update Assessment Answers"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/answers'
    return request.put(base_url, headers, root+path, name, payload)

def get_assessment_reviewers(base_url, headers, tenantId, clientId, assessmentId):
    """
    This request **retrieves a list of reviewers** for a an assessment.
    """
    name = "Get Assessment Reviewers"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/reviewers'
    return request.get(base_url, headers, root+path, name)

def create_client_assessment(base_url, headers, tenantId, clientId, payload):
    """
    This request **creates** a new assessment for a specific client within a tenant.

The `instanceUrl` , `tenantId` and `clientId` is needed to execute the call.

**NOTE:** It is recommended to first obtain the questionnaire and view the JSON structure needed for the specific assessment.

**NOTE:** This endpoint is meant to create a new Client Assessment from an existing Questionnaire. To reopen a completed Client Assessment see [Copy Client Assessment](https://api-docs.plextrac.com/#499773c6-7a7a-4188-946d-3f1921bcfc7f)

Below is returned on a successful call:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| message | validation of request | success |
| doc_id | generated assessment ID | assessment_3458_tenant_0_client_1912 |
    """
    name = "Create Client Assessment"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment'
    return request.post(base_url, headers, root+path, name, payload)

def update_client_assessment(base_url, headers, tenantId, clientId, assessmentId, payload):
    """
    This request **updates** an assessment.

The `instanceUrl` , `tenantId`, `assessmentId` and `clientId` is needed to execute the call.
    """
    name = "Update Client Assessment"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_client_assessment(base_url, headers, tenantId, clientId, assessmentId):
    """
    This request will **delete** an assessment for a client.

The `instanceUrl` , `tenantId`, `assessmentId` and `clientId` is needed to execute the call.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | status of delete call | success |
| data |  |  |
| message | validation of delete request | success |
| doc_id | ID of assessment deleted | assessment_3098_tenant_0_client_1912 |
    """
    name = "Delete Client Assessment"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'
    return request.delete(base_url, headers, root+path, name)

def create_report_from_assessment_questionnaire(base_url, headers, tenantId, clientId, assessmentId, payload):
    """
    This request will **create a report** from assessments for a client.

The `instanceUrl` , `tenantId`, `assessmentId` and `clientId` is needed to execute the call.

Using this endpoint will not delete the assessment.

Leaving the 'answers' value blank will submit the answers currently on the assessment. Use other endpoints to change an assessment question's answers **before** using this call, if answers need to be modified.

When successful, the following parameters will be returned:

| **parameter** | **definition** | **example value** |
| --- | --- | --- |
| status | status of call | success |
| data |  |  |
| status | status of call | success |
| message | validation of delete request | full report created successfully |
| report_id | generated report ID | 35228 |
    """
    name = "Create Report From Assessment Questionnaire"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}/report'
    return request.post(base_url, headers, root+path, name, payload)

def copy_asessment_questionnaire(base_url, headers, tenantId, clientId, assessmentId, payload):
    """
    This request **creates a new assessment** from a previously completed assessment, copying over questions and answers.
    """
    name = "Copy Asessment Questionnaire"
    root = "/api/v2"
    path = f'/tenants/{tenantId}/clients/{clientId}/assessments/{assessmentId}/copy'
    return request.post(base_url, headers, root+path, name, payload)
