import logging


# logging
console_log_level = logging.DEBUG
file_log_level = logging.INFO
save_logs_to_file = True

# requests
# if the Plextrac instance is running on https without valid certs, requests will respond with cert error
# change this to false to override verification of certs
verify_ssl = True

# description of script that will be print line by line when the script is run
script_info = ["====================================================================",
               "= General CSV Import Script                                        =",
               "=------------------------------------------------------------------=",
               "= Takes a CSV with rows representing client, report, finding and   =",
               "= asset data and a CSV with how to map each column to a            =",
               "= location in Plextrac. Parses the CSV and import data to Plextrac =",
               "===================================================================="
            ]


