import logging


# LOGGING
console_log_level = logging.INFO
file_log_level = logging.INFO
save_logs_to_file = False

# REQUESTS
# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True
# number of times to rety a request before throwing an error. will only throw the last error encountered if
# number of retries is exceeded. set to 0 to disable retrying requests
retries = 5

# description of script that will be print line by line when the script is run
script_info = ["====================================================================",
               "= Base API Script                                                  =",
               "=------------------------------------------------------------------=",
               "= Use this script as a starting point to utilize existing          =",
               "= funtionality when developing a script for the Plextrac API       =",
               "=                                                                  =",
               "===================================================================="
            ]
