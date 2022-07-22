from operator import itemgetter

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
    
    base_url, cf_token = itemgetter('base_url', 'cf_token')(handle_instance_url())

    auth = Auth(base_url)
    if cf_token != None:
        auth.add_cf_auth_header(cf_token)
    auth.handle_auth()
    
    print("\nStart Script Here")
