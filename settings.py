import logging


# logging
console_log_level = logging.INFO
file_log_level = logging.INFO
save_logs_to_file = False

# requests
# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True

# description of script that will be print line by line when the script is run
script_info = ["====================================================================",
               "= Base Script                                                      =",
               "=------------------------------------------------------------------=",
               "= Use this script as a starting point to utilize existing          =",
               "= funtionality when developing a script for the Plextrac API       =",
               "=                                                                  =",
               "===================================================================="
            ]
