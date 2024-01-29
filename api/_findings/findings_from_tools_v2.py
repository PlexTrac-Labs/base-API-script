from utils import request_handler as request

def add_findings_from_file_imports_v2(base_url, headers, clientId, reportId, source, payload):
    """
    This endpoint will be added in the **1.61 release**.

`source` must be from the following list:

acunetix  
burp  
burphtml  
checkmarx  
coreimpact  
custom  
hclappscan Scan  
horizon  
invicti  
nessus  
netsparker  
nexpose  
nipper  
nmap  
nodeware  
nodezero  
offlinecsv  
openvas  
owaspzap  
pentera  
ptrac  
qualys  
rapidfire  
scythe  
veracode
    """
    name = "Add Findings from File Imports V2"
    root = "/api/v2"
    path = f'/client/{clientId}/report/{reportId}/importAsync/{source}'
    return request.post(base_url, headers, root+path, name, payload)
