import re
import time

import settings
log = settings.log


def format_key(str):
    return re.sub('[\W]', '', re.sub('[ -]', '_', str.lower()))

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