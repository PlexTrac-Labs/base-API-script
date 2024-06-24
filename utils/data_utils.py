from copy import deepcopy

import utils.log_handler as logger
log = logger.log
from utils.auth_handler import Auth
import utils.input_utils as input
import api

def get_page_of_clients(page: int = 0, clients: list = [], total_clients: int = -1, auth:Auth=None) -> bool:
    """
    Handles traversing pagination results to create a list of all items.

    :param page: page to start on, for all results use 0, defaults to 0
    :type page: int, optional
    :param clients: the list passed in will be added to, acts as return, defaults to []
    :type clients: list, optional
    :param total_clients: used for recursion to know when all pages have been gathered, defaults to -1
    :type total_clients: int, optional
    :param auth: Auth object for API requests
    :type auth: Auth
    :return: boolean if all page requests were successful
    :rtype: bool
    """
    payload = {
        "pagination": {
            "offset": page*100,
            "limit": 100
        }
    }
    # region - full structure of client data response

    # {
    #     "status": "success",
    #     "data": [
    #         {
    #             "cuid": "clcm94d8c00040io2g3qnbhfe",
    #             "tenant_id": 0,
    #             "client_id": 1045,
    #             "name": "Green Testing",
    #             "poc": "point of contact",
    #             "poc_email": "test@email.com",
    #             "custom_field": [
    #                 {
    #                     "label": "Custom Field Label",
    #                     "value": "value"
    #                 }
    #             ],
    #             "tags": [
    #                 "test_tag"
    #             ],
    #             "logo": "",
    #             "description": "Client Description / Details",
    #             "doc_type": "client",
    #             "users": {
    #                 "test.user@plextrac.com": {
    #                     "role": "ADMIN",
    #                     "classificationId": null
    #                 }
    #             }
    #         }
    #     ],
    #     "meta": {
    #         "pagination": {
    #             "offset": 0,
    #             "limit": 25,
    #             "total": 1
    #         },
    #         "sort": [
    #             {
    #                 "by": "name",
    #                 "order": "ASC"
    #             }
    #         ],
    #         "filters": [
    #             {
    #                 "by": "tags",
    #                 "value": [
    #                     "test_tag"
    #                 ]
    #             }
    #         ]
    #     }
    # }
    # endregion
    try:
        response = api.clients.list_clients(auth.base_url, auth.get_auth_headers(), payload)
        if response.json.get("status") != "success":
            log.exception(f'Could not retrieve clients from instance')
            return False
    except Exception as e:
        log.exception(e)
        return False
    
    total_clients = int(response.json['meta']['pagination']['total'])
    if len(response.json['data']) > 0:
        clients += deepcopy(response.json['data'])

    if len(clients) < total_clients:
        return get_page_of_clients(page+1, clients, total_clients, auth=auth)
    
    return True

def get_page_of_reports(page: int, reports: list = [], total_reports: int = -1, auth:Auth=None) -> None:
    """
    Handles traversing pagination results to create a list of all items.

    :param page: page to start on, for all results use 0, defaults to 0
    :type page: int, optional
    :param reports: the list passed in will be added to, acts as return, defaults to []
    :type reports: list, optional
    :param total_reports: used for recursion to know when all pages have been gathered, defaults to -1
    :type total_reports: int, optional
    :param auth: Auth object for API requests
    :type auth: Auth
    :return: boolean if all page requests were successful
    :rtype: bool
    """
    payload = {
        "pagination": {
            "offset": page*1000,
            "limit": 1000
        }
    }
    # region - full structure of report data response
    
    # {
    #     "status": "success",
    #     "data": [
    #         {
    #             "id": 345951070,
    #             "cuid": "clw8551rq01cd0gjz9yy3c8zw",
    #             "client_id": 1045,
    #             "name": "Test Report",
    #             "status": "Published",
    #             "created_at": 1715796843831,
    #             "fields_template": "82dd7c33-9da8-416d-b186-2de37261c0f8",
    #             "tags": [
    #                 "test_tag",
    #                 "green_testing"
    #             ],
    #             "reviewers": [
    #                 "test.user@plextrac.com"
    #             ],
    #             "classificationTierId": null,
    #             "template": "eb91b9c2-86e7-4fde-b8b3-a8d77fe958cf",
    #             "description": null,
    #             "logistics": "",
    #             "reportType": "default",
    #             "includeEvidence": false,
    #             "start_date": "2024-06-17T20:25:33.537Z",
    #             "end_date": "2024-06-24T20:25:35.706Z",
    #             "exec_summary": {
    #                 "custom_fields": [
    #                     {
    #                         "id": "clw8551sr01cf0gjze5wf50qt",
    #                         "label": "New Narrative",
    #                         "tags": [
    #                             "test_tag"
    #                         ],
    #                         "text": "<p>text</p>",
    #                         "repository": null,
    #                         "isFromNarrativesDB": false,
    #                         "titleCommentThreadId": null,
    #                         "cuid": "clw8551sr01cg0gjzdnjqd2rf"
    #                     }
    #                 ]
    #             },
    #             "custom_field": [
    #                 {
    #                     "label": "Custom Field Lable",
    #                     "value": "value"
    #                 }
    #             ],
    #             "operators": [
    #                 "test.user@plextrac.com"
    #             ],
    #             "isTrackChanges": false,
    #             "findings": 6,
    #             "fields_template_name": "Green Testing Findings Template",
    #             "template_name": "Green Test Report Template"
    #         }
    #     ],
    #     "meta": {
    #         "pagination": {
    #             "offset": 0,
    #             "limit": 25,
    #             "total": 1
    #         },
    #         "sort": [
    #             {
    #                 "by": "name",
    #                 "order": "ASC"
    #             }
    #         ],
    #         "filters": [
    #             {
    #                 "by": "clients",
    #                 "value": [
    #                     1045
    #                 ]
    #             }
    #         ]
    #     }
    # }

    # endregion
    try:
        response = api.reports.get_report_list(auth.base_url, auth.get_auth_headers(), payload)
        if response.json['status'] != "success":
            log.exception(f'Could not retrieve reports from instance')
            return False
    except Exception as e:
        log.exception(e)
        return False
    
    total_reports = int(response.json['meta']['pagination']['total'])
    if len(response.json['data']) > 0:
        reports += deepcopy(response.json['data'])

    if len(reports) < total_reports:
        return get_page_of_reports(page+1, reports, total_reports, auth=auth)
    
    return True

def get_page_of_assets(page: int = 0, assets: list = [], total_assets: int = -1, auth:Auth=None) -> None:
    """
    Handles traversing pagination results to create a list of all items.

    :param page: page to start on, for all results use 0, defaults to 0
    :type page: int, optional
    :param assets: the list passed in will be added to, acts as return, defaults to []
    :type assets: list, optional
    :param total_assets: used for recursion to know when all pages have been gathered, defaults to -1
    :type total_assets: int, optional
    :param auth: Auth object for API requests
    :type auth: Auth
    :return: boolean if all page requests were successful
    :rtype: bool
    """
    payload = {
        "pagination": {
            "offset": page*1000,
            "limit": 1000
        }
    }
    # region - full structure of asset data response
    
    # {
    #     "status": "success",
    #     "assets": [
    #         {
    #             "asset": "Test Asset",
    #             "assetCriticality": "High",
    #             "clientId": 1045,
    #             "createdAt": 1719262029680,
    #             "cuid": "clxtg809r02c90gmp3aoc60iw",
    #             "dataOwner": "Data Owner",
    #             "description": "<p><span style=\"background-color:rgb(255,255,255);color:rgb(37,36,40);\">Asset Description</span></p>",
    #             "dnsName": "DNS Name",
    #             "hostFqdn": "Host FQDN",
    #             "hostname": "Hostname",
    #             "hostRdns": "Host RDNS",
    #             "id": "clxtg809r02c90gmp3aoc60iw",
    #             "knownIps": [
    #                 "1.1.1.1"
    #             ],
    #             "macAddress": "MAC Address",
    #             "netbiosName": "NetBIOS Name",
    #             "notes": [],
    #             "operatingSystems": [
    #                 "windows"
    #             ],
    #             "pciStatus": "pass",
    #             "physicalLocation": "Physical Location",
    #             "ports": {
    #                 "1234_service_protocol_version": {
    #                     "number": "1234",
    #                     "protocol": "protocol",
    #                     "service": "service",
    #                     "version": "version"
    #                 }
    #             },
    #             "systemOwner": "System Owner",
    #             "tags": [
    #                 "test_tag",
    #                 "green_testing"
    #             ],
    #             "totalCves": 1,
    #             "type": "Workstation",
    #             "updatedAt": 1719262029680,
    #             "parentName": "",
    #             "findings": {}
    #         }
    #     ],
    #     "meta": {
    #         "pagination": {
    #             "total": 1,
    #             "offset": 0,
    #             "limit": 5
    #         },
    #         "sort": [
    #             {
    #                 "by": "asset",
    #                 "order": "DESC"
    #             }
    #         ],
    #         "filters": [
    #             {
    #                 "by": "tags",
    #                 "value": [
    #                     "test_tag",
    #                     "green_testing"
    #                 ]
    #             }
    #         ]
    #     }
    # }

    # endregion
    try:
        response = api.assets.get_tenant_assets(auth.base_url, auth.get_auth_headers(), payload)
        if response.json['status'] != "success":
            log.exception(f'Could not retrieve assets from instance')
            return False
    except Exception as e:
        log.exception(e)
        return False
    
    total_assets = int(response.json['meta']['pagination']['total'])
    if len(response.json['assets']) > 0:
        assets += deepcopy(response.json['assets'])

    if len(assets) < total_assets:
        return get_page_of_assets(page+1, assets, total_assets, auth=auth)
    
    return True

def get_page_of_report_findings(client_id: int, report_id: int, page: int = 0, findings: list = [], total_findings: int = -1, auth:Auth=None) -> bool:
    """
    Handles traversing pagination results to create a list of all finding in a report.

    :param client_id: id of client
    :type client_id: int
    :param report_id: id of report
    :type report_id: int
    :param page: page to start on, for all results use 0, defaults to 0
    :type page: int, optional
    :param findings: the list passed in will be added to, acts as return, defaults to []
    :type findings: list, optional
    :param total_findings: used for recursion to know when all pages have been gathered, defaults to -1
    :type total_findings: int, optional
    :param auth: Auth object for API requests
    :type auth: Auth
    :return: boolean if all page requests were successful
    :rtype: bool
    """
    payload = {
        "pagination": {
            "offset": page*100,
            "limit": 100
        }
    }
    # region - full structure of finding data response

    # {
    #     "status": "success",
    #     "data": [
    #         {
    #             "affected_assets": {
                    # region - affected asset info
    #                 "clxtg809r02c90gmp3aoc60iw": {
    #                     "cuid": "clxtg809r02c90gmp3aoc60iw",
    #                     "asset": "Test Asset",
    #                     "assetCriticality": "High",
    #                     "assignedTo": null,
    #                     "closedAt": null,
    #                     "createdAt": 1719262029680,
    #                     "description": "<p><span style=\"background-color:rgb(255,255,255);color:rgb(37,36,40);\">Asset Description</span></p>",
    #                     "evidence": [
    #                         "cc62cefd-43d7-4851-a629-3f25b1488188"
    #                     ],
    #                     "exhibits": [],
    #                     "hostname": "Hostname",
    #                     "host_fqdn": "Host FQDN",
    #                     "host_rdns": "Host RDNS",
    #                     "id": "clxtg809r02c90gmp3aoc60iw",
    #                     "knownIps": [
    #                         "1.1.1.1"
    #                     ],
    #                     "locationUrl": "Location/URL",
    #                     "mac_address": "MAC Address",
    #                     "netbios_name": "NetBIOS Name",
    #                     "notes": "notes",
    #                     "operating_system": [
    #                         "windows"
    #                     ],
    #                     "ports": {
    #                         "1234_service_protocol_version": {
    #                             "number": "1234",
    #                             "service": "service",
    #                             "protocol": "protocol",
    #                             "version": "version"
    #                         }
    #                     },
    #                     "reopenedAt": null,
    #                     "status": "Open",
    #                     "subStatus": "",
    #                     "tags": [
    #                         "test_tag",
    #                         "green_testing"
    #                     ],
    #                     "total_cves": "1",
    #                     "updatedAt": 1719263755107,
    #                     "vulnerableParameters": [
    #                         {
    #                             "id": "clxth8i9m000c356un00umgkw",
    #                             "text": "param=52"
    #                         }
    #                     ],
    #                     "client_id": 1045,
    #                     "data_owner": "Data Owner",
    #                     "dns_name": "DNS Name",
    #                     "pci_status": "pass",
    #                     "physical_location": "Physical Location",
    #                     "system_owner": "System Owner",
    #                     "type": "Workstation",
    #                     "findings": {
    #                         "1795388512": {
    #                             "id": 1795388512,
    #                             "client_id": 1045,
    #                             "createdAt": 1719262029680,
    #                             "cuid": "clxtgh5d101tk0hle4bn7dnxm",
    #                             "updatedAt": 1719263754923,
    #                             "closedAt": null,
    #                             "reopenedAt": null,
    #                             "title": "Test Finding",
    #                             "severity": "Low",
    #                             "status": "Open",
    #                             "subStatus": "",
    #                             "assignedTo": null,
    #                             "instances": {
    #                                 "345951070": {
    #                                     "report_id": 345951070,
    #                                     "report_severity": "Low",
    #                                     "report_status": "Open",
    #                                     "report_flaw_title": "Test Finding",
    #                                     "report_flaw_visibility": "draft",
    #                                     "createdAt": 1719262456165,
    #                                     "updatedAt": 1719262674044
    #                                 }
    #                             },
    #                             "ports": {
    #                                 "1234_service_protocol_version": {
    #                                     "number": "1234",
    #                                     "service": "service",
    #                                     "protocol": "protocol",
    #                                     "version": "version"
    #                                 }
    #                             },
    #                             "locationUrl": "Location/URL",
    #                             "vulnerableParameters": [
    #                                 {
    #                                     "id": "clxth8i9m000c356un00umgkw",
    #                                     "text": "param=52"
    #                                 }
    #                             ],
    #                             "notes": "notes",
    #                             "evidence": [
    #                                 "cc62cefd-43d7-4851-a629-3f25b1488188"
    #                             ]
    #                         }
    #                     }
    #                 }
                    # endregion
    #             },
    #             "assignedTo": "test.user@plextrac.com",
    #             "client_id": 1045,
    #             "client_name": "",
    #             "code_samples": [],
    #             "common_identifiers": {
    #                 "CVE": [
    #                     {
    #                         "id": 5463,
    #                         "link": "https://www.cve.org/CVERecord?id=CVE-2023-5463",
    #                         "name": "CVE-2023-5463",
    #                         "year": 2023
    #                     }
    #                 ],
    #                 "CWE": [
    #                     {
    #                         "id": 1352,
    #                         "link": "https://cwe.mitre.org/data/definitions/1352.html",
    #                         "name": "CWE-1352"
    #                     }
    #                 ]
    #             },
    #             "createdAt": 1719262456165,
    #             "description": "<p><span style=\"background-color:rgb(255,255,255);color:rgb(37,36,40)\">Description</span></p>",
    #             "doc_type": "flaw",
    #             "doc_version": "2.6.7",
    #             "exhibits": [],
    #             "flaw_id": 1795388512,
    #             "last_update": 1719262674044,
    #             "reopenedAt": 1719263706639,
    #             "report_id": 345951070,
    #             "report_name": "",
    #             "sev": 3,
    #             "severity": "Low",
    #             "severity_key": 3,
    #             "source": "plextrac",
    #             "status": "Open",
    #             "title": "Test Finding",
    #             "visibility": "draft",
    #             "closedAt": null,
    #             "fields": {
    #                 "retest": {
    #                     "id": "clxtgh5d301tn0hle3mqxcu79",
    #                     "key": "retest",
    #                     "label": "Retest",
    #                     "value": "<p>value</p>",
    #                     "sort_order": 0
    #                 },
    #                 "scores": {
    #                     "cvss3": {
    #                         "type": "cvss3",
    #                         "label": "3.0 label",
    #                         "value": "5",
    #                         "calculation": "3.0 calc"
    #                     },
    #                     "cvss": {
    #                         "type": "cvss",
    #                         "label": "2.0 label",
    #                         "value": "5",
    #                         "calculation": "2.0 calc"
    #                     },
    #                     "general": {
    #                         "type": "general",
    #                         "label": "general label",
    #                         "value": "5",
    #                         "calculation": "general calc"
    #                     }
    #                 }
    #             },
    #             "id": 1795388512,
    #             "jiraIssue": null,
    #             "recommendations": "<p><span style=\"background-color:rgb(255,255,255);color:rgb(37,36,40)\">Recommendations</span></p>",
    #             "references": "<p><span style=\"background-color:rgb(255,255,255);color:rgb(37,36,40)\">References</span></p>",
    #             "selectedScore": "cvss4",
    #             "serviceNowTicket": null,
    #             "subStatus": "Updated",
    #             "tags": [
    #                 "test_tag",
    #                 "green_testing"
    #             ],
    #             "tenant_id": 0,
    #             "risk_score": {
    #                 "CVSS2": {
    #                     "vector": "2.0 calc",
    #                     "overall": 5,
    #                     "subScore": {
    #                         "base": 5
    #                     }
    #                 },
    #                 "CVSS3": {
    #                     "vector": "3.0 calc",
    #                     "overall": 5,
    #                     "subScore": {
    #                         "base": 5
    #                     }
    #                 },
    #                 "CVSS4": {
    #                     "vector": "AV:A/AC:H/AT:P/PR:N/UI:A/VC:L/VI:H/VA:N/SC:L/SI:L/SA:L/E:U",
    #                     "overall": 1.9
    #                 },
    #                 "CVSS3_1": {
    #                     "vector": "AV:N/AC:H/PR:L/UI:R/S:C/C:N/I:L/A:N",
    #                     "overall": 3,
    #                     "subScore": {
    #                         "base": 3,
    #                         "temporal": 3,
    #                         "environmental": 3
    #                     }
    #                 }
    #             },
    #             "calculated_severity": true,
    #             "reportedAt": 1719262456165,
    #             "finding_id": null,
    #             "cuid": "clxtgh5d101tk0hle4bn7dnxm",
    #             "jiraIssueKey": null,
    #             "jiraIssueLink": null,
    #             "serviceNowTicketKey": null,
    #             "serviceNowTicketTable": null,
    #             "timeToNearestSLA": "",
    #             "prioritiesSample": {
    #                 "priorities": [],
    #                 "total": 0
    #             }
    #         }
    #     ],
    #     "meta": {
    #         "pagination": {
    #             "total": 1,
    #             "offset": 0,
    #             "limit": 10
    #         },
    #         "filters": [
    #             {
    #                 "by": "findingTags",
    #                 "value": [
    #                     "test_tag",
    #                     "green_testing"
    #                 ]
    #             }
    #         ],
    #         "sort": [
    #             {
    #                 "by": "title",
    #                 "order": "ASC"
    #             },
    #             {
    #                 "by": "status",
    #                 "order": "DESC"
    #             },
    #             {
    #                 "by": "severity",
    #                 "order": "ASC"
    #             }
    #         ],
    #         "flawIds": [
    #             1795388512
    #         ]
    #     }
    # }

    # endregion
    try:
        response = api.findings.get_findings_by_report(auth.base_url, auth.get_auth_headers(), client_id, report_id, payload)
        if response.json['status'] != "success":
            log.exception(f'Could not retrieve findings from report')
            return False
    except Exception as e:
        log.exception(e)
        return False
    
    total_findings = int(response.json['meta']['pagination']['total'])
    if len(response.json['data']) > 0:
        findings += deepcopy(response.json['data'])

    if len(findings) < total_findings:
        return get_page_of_report_findings(client_id, report_id, page+1, findings, total_findings, auth=auth)
    
    return True


def get_writeups(writeups: list = [], auth:Auth=None) -> bool:
    """
    Gets a list of all writeups from tenant

    :param writeups: the list passed in will be added to, acts as return, defaults to []
    :type writeups: list, optional
    :param auth: Auth object for API requests
    :type auth: Auth
    :return: boolean if all page requests were successful
    :rtype: bool
    """
    # region - full structure of writeup data response
    
    # [
    #     {
    #         "cuid": "cltiy6sry00yg0hpg24yt8omd",
    #         "createdAt": 1709919950346,
    #         "createdBy": 905,
    #         "description": "<p>description</p>",
    #         "doc_id": 297824,
    #         "doc_type": "template",
    #         "fields": {
    #             "scores": {},
    #             "my_custom_field": {
    #                 "label": "My Custom Field",
    #                 "value": "<p>custom field value</p>",
    #                 "id": "cltiy7hzu005i0hr25i3le42q"
    #             }
    #         },
    #         "isDeleted": false,
    #         "id": "template_297824",
    #         "repositoryId": "clp32v4x0006t0ho5erd3fwz7",
    #         "recommendations": "<p>recommendations</p>",
    #         "references": "<p>references</p>",
    #         "severity": "Medium",
    #         "score": "",
    #         "source": "Custom",
    #         "tenantId": 0,
    #         "title": "Sample Writeup",
    #         "tags": [
    #             "test_tag"
    #         ],
    #         "updatedAt": 1709919996584,
    #         "writeupAbbreviation": "TES-12",
    #         "common_identifiers": {
    #             "CVE": [
    #                 {
    #                     "name": "CVE-2023-43717",
    #                     "year": 2023,
    #                     "id": 43717,
    #                     "link": "https://www.cve.org/CVERecord?id=CVE-2023-43717"
    #                 },
    #                 {
    #                     "name": "CVE-2023-40273",
    #                     "year": 2023,
    #                     "id": 40273,
    #                     "link": "https://www.cve.org/CVERecord?id=CVE-2023-40273"
    #                 }
    #             ],
    #             "CWE": [
    #                 {
    #                     "name": "CWE-1234",
    #                     "id": 1234,
    #                     "link": "https://cwe.mitre.org/data/definitions/1234.html"
    #                 },
    #                 {
    #                     "name": "CWE-1035",
    #                     "id": 1035,
    #                     "link": "https://cwe.mitre.org/data/definitions/1035.html"
    #                 }
    #             ]
    #         },
    #         "risk_score": {
    #             "CVSS3_1": {
    #                 "overall": 5,
    #                 "subScore": {
    #                     "base": 5,
    #                     "temporal": 5,
    #                     "environmental": 5
    #                 },
    #                 "vector": "AV:L/AC:H/PR:L/UI:R/S:C/C:L/I:L/A:L"
    #             }
    #         },
    #         "calculated_severity": true
    #     }
    # ]

    # endregion
    try:
        response = api._content_library._writeupsdb.writeups.list_writeups(auth.base_url, auth.get_auth_headers())
        writeups += deepcopy(response.json)
        return True
    except Exception as e:
        log.exception(e)
        return False

def get_client_choice(clients) -> int:
    """
    Prompts the user to select from a list of clients.
    Based on subsequently called functions, this will return a valid option or exit the script.

    :param repos: List of clients returned from the POST List Clients endpoint
    :type repos: list[client objects]
    :return: 0-based index of selected client from the list provided
    :rtype: int
    """
    log.info(f'List of Clients:')
    index = 1
    for client in clients:
        log.info(f'{index} - Name: {client["name"]} | ID: {client["client_id"]} | Tags: {client.get("tags", [])}')
        index += 1
    return input.user_list("Select a client", "Invalid choice", len(clients)) - 1

def get_report_choice(reports) -> int:
    """
    Prompts the user to select from a list of reports.
    Based on subsequently called functions, this will return a valid option or exit the script.

    :param repos: List of reports returned from the POST List Reports endpoint
    :type repos: list[report objects]
    :return: 0-based index of selected report from the list provided
    :rtype: int
    """
    log.info(f'List of Reports:')
    index = 1
    for report in reports:
        log.info(f'{index} - Name: {report["name"]} | ID: {report["id"]} | Status: {report["status"]} | Num Findings: {report["findings"]} | Tags: {report.get("tags", [])}')
        index += 1
    return input.user_list("Select a report", "Invalid choice", len(reports)) - 1
