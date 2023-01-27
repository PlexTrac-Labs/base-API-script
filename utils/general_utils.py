import re
import time
from hashlib import sha256

import utils.log_handler as logger
log = logger.log


def format_key(str):
    new_str = str.strip().lower()
    return re.sub('[\W]', '', re.sub('[ -]', '_', new_str))

def add_tag(list, tag):
    new_tag = format_key(tag)
    if new_tag not in list:
        list.append(new_tag)

def try_parsing_date(possible_date_str, field):
    """
    Try to parse a date using several formats, warn about
    problematic value if the possible_date does not match
    any of the formats tried
    """
    for fmt in ('%m/%d/%Y', '%m-%d-%Y', '%m/%d/%y', '%m-%d-%y', '%Y/%m/%d', '%Y-%m-%d', '%m/%d/%Y %I:%M:%S %p'):
        try:
            return time.strptime(possible_date_str, fmt)
        except ValueError:
            pass
    log.warning(f"Non-valid date format for '{field}': '{possible_date_str}'. Ignoring...")
    return None

def is_str_positive_integer(value):
    try:
        value = int(value)
        if value < 1:
            raise ValueError
    except ValueError as e:
        return False
    return True

def is_valid_ipv4_address(address): 
    pattern = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$" 
    if re.match(pattern, address): 
        return True 
    else:
        return False 

def is_valid_cve(cve):
    cve_pattern = re.compile(r'CVE-[0-9]{4}-[0-9]')
    return cve_pattern.match(cve) is not None

def is_valid_cwe(cwe):
    cwe_pattern = re.compile(r'CWE-[0-9]')
    pattern_match = cwe_pattern.match(cwe) is not None
    cwe_num = re.compile(r'[0-9]')
    num_match = cwe_num.match(cwe) is not None
    return pattern_match or num_match

def sanitize_name_for_file(name):
    # certain characters are not allowed in file names
    invalid_chars = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]
    
    new_name = name
    for char in invalid_chars:
        new_name = new_name.replace(char, "")

    return new_name.replace(" ", "_")

def generate_flaw_id(title):
    return int(sha256(title.encode('utf-8')).hexdigest(), 16) % 10 ** 8
    