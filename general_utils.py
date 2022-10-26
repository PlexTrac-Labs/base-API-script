import re
import time


def format_key(str):
    return re.sub('[\W]', '', re.sub('[ -]', '_', str.lower()))

def add_tag(list, tag):
    new_tag = format_key(tag)
    if new_tag not in list:
        list.append(new_tag)

def try_parsing_date(log, possible_date_str, field):
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
    log.exception(f"Non-valid date format for '{field}': '{possible_date_str}'. Ignoring...")
    return None

