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

    auth = Auth(args)
    auth.handle_authentication()
    

    # Starting from this authentication example, you can now build out your script and call other endpoints


    # Authorization verification is built in through the get_auth_headers() method
    # After the 2 lines above setting up the auth object, `auth.get_auth_headers()' will return the headers needed to add to any API calls
    print("\nCompleted with auth_headers: ", auth.get_auth_headers())
