from utils import request_handler as request

def add_findings_from_file_imports(base_url, headers, clientId, reportId, source, payload):
    """
    source must be from the following list:

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
    name = "Add Findings from File Imports"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/{source}'
    return request.post(base_url, headers, root+path, name, payload)

def import_acunetix(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Acunetix.
    """
    name = "Import Acunetix"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/acunetix'
    return request.post(base_url, headers, root+path, name, payload)

def import_burp(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Burp.
    """
    name = "Import Burp"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/burp'
    return request.post(base_url, headers, root+path, name, payload)

def import_core_impact(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Core Impact.
    """
    name = "Import Core Impact"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/coreimpact'
    return request.post(base_url, headers, root+path, name, payload)

def import_nessus_file(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Nessus.
    """
    name = "Import Nessus File"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/nessus'
    return request.post(base_url, headers, root+path, name, payload)

def import_netsparker(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Netsparker.
    """
    name = "Import Netsparker"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/netsparker'
    return request.post(base_url, headers, root+path, name, payload)

def import_nexpose(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Nexpose.
    """
    name = "Import Nexpose"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/nexpose'
    return request.post(base_url, headers, root+path, name, payload)

def import_nipper(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Nipper.
    """
    name = "Import Nipper"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/nipper'
    return request.post(base_url, headers, root+path, name, payload)

def import_nmap(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Nmap (Vulners NSE).
    """
    name = "Import Nmap"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/nmap'
    return request.post(base_url, headers, root+path, name, payload)

def import_openvas(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool OpenVAS.
    """
    name = "Import OpenVAS"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/openvas'
    return request.post(base_url, headers, root+path, name, payload)

def import_qualys(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Qualys.
    """
    name = "Import Qualys"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/qualys'
    return request.post(base_url, headers, root+path, name, payload)

def import_rapidfire(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool RapidFire.
    """
    name = "Import RapidFire"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/rapidfire'
    return request.post(base_url, headers, root+path, name, payload)

def import_scythe(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool SCYTHE.
    """
    name = "Import SCYTHE"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/scythe'
    return request.post(base_url, headers, root+path, name, payload)

def import_veracode(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** from the tool Vercode.
    """
    name = "Import Veracode"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/veracode'
    return request.post(base_url, headers, root+path, name, payload)

def import_ptrac(base_url, headers, clientId, reportId, payload):
    """
    This request **imports findings** that is in PTRAC format.
    """
    name = "Import PTRAC"
    root = "/api/v1"
    path = f'/client/{clientId}/report/{reportId}/import/ptrac'
    return request.post(base_url, headers, root+path, name, payload)
