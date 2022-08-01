from operator import itemgetter
import yaml

from input_utils import *
from auth_utils import *
from request_utils import *


script_info = ["===================================================================",
               "= Example Authentication Script                                   =",
               "=-----------------------------------------------------------------=",
               "=  Walks the user through the process of getting auth info, then  =",
               "=  validates the info with Plextrac's authenticate endpoints.     =",
               "=                                                                 =",
               "=  Future link to documentation                                   =",
               "=  Future link to Plextrac Labs example scripts                   =",
               "==================================================================="
            ]


if __name__ == '__main__':
    for i in script_info:
        print(i)

    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)

    username = args.get('username')
    password = args.get('password')
    
    base_url, cf_token = itemgetter('base_url', 'cf_token')(handle_instance_url(args))

    auth = Auth(base_url)
    if cf_token != None:
        auth.add_cf_auth_header(cf_token)
    auth.username = username
    auth.password = password
    
    auth.handle_auth()
    
    # Starting from this authentication example, you can now start your script and call other endpoints
    # Pass in the `auth.auth_headers` as the headers for any API requests
