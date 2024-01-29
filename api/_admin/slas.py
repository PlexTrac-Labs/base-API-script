from utils import request_handler as request

def get_sla_benchmarks(base_url, headers):
    """
    This request retrieves **all** SLA benchamrks for a tenant.

The `instanceUrl` is needed to execute the call.
    """
    name = "Get SLA Benchmarks"
    root = "/api/v2"
    path = f'/sla/benchmarks'
    return request.get(base_url, headers, root+path, name)

def create_sla_benchmark(base_url, headers, payload):
    """
    This request **creates** a new SLA benchmark within a tenant.

The `name`, `daysToClose`, `findingSeverity`, and `enabled` are required properties.
    """
    name = "Create SLA Benchmark"
    root = "/api/v2"
    path = f'/sla/benchmarks'
    return request.post(base_url, headers, root+path, name, payload)

def get_sla_benchmark(base_url, headers, slaBenchmarkId):
    """
    This request retrieves information on a SLA benchmark.

#### Request Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| slaBenchmarkId | Integer | The ID of the SLA to retrieve |

A successsfull call returns the JSON object of the SLA benchmark stored in the DB.
    """
    name = "Get SLA Benchmark"
    root = "/api/v2"
    path = f'/sla/benchmarks/{slaBenchmarkId}'
    return request.get(base_url, headers, root+path, name)

def update_sla_benchmark(base_url, headers, slaBenchmarkId, payload):
    """
    This request updates an existing SLA benchamrk. This is a PUT request and will overwrite the current SLA with the new payload.

#### Request Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| slaBenchmarkId | String | The unique identifier of the SLA to be updated |

#### Request Payload

You should use the Get SLA Benchmark endpoint to get the SLA object, then use that JSON object as the payload.

You must remove the `doc_type` and `tenant_id` properties before sending hte payload.

#### Response Fields

In the event of a successful request, the response will contain the following fields:

| Parameter | Type | Description |
| --- | --- | --- |
| status | String | The status of the request |
| data | String | The ID of the SLA that was updated |

In the event of an error, the response will contain an 'error' object with a 'message' field describing the error.
    """
    name = "Update SLA Benchmark"
    root = "/api/v2"
    path = f'/sla/benchmarks/{slaBenchmarkId}'
    return request.put(base_url, headers, root+path, name, payload)

def delete_sla_benchmark(base_url, headers, slaBenchmarkId):
    """
    This request **removes** a SLA benchmark from a tenant.

The `instanceUrl` and `slaBenchamrkId` is needed to execute the call.
    """
    name = "Delete SLA Benchmark"
    root = "/api/v2"
    path = f'/sla/benchmarks/{slaBenchmarkId}'
    return request.delete(base_url, headers, root+path, name)
