from utils import request_handler as request

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

def get_client_assessment(base_url, headers, tenantId, clientId, assessmentId):
    """
    This request retrieves a list of **a specific** assessment for **a specific client** within a tenant.

The `instanceUrl` , `tenantId` , `clientId`, and `assessmentID` is needed to execute the call.
    """
    name = "Get Client Assessment"
    root = "/api/v1"
    path = f'/tenant/{tenantId}/client/{clientId}/assessment/{assessmentId}'
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
