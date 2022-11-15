import yaml

from auth_utils import *


script_info = ["===================================================================",
               "= Example Authentication Script                                   =",
               "=-----------------------------------------------------------------=",
               "=  Walks the user through the process of getting auth info, then  =",
               "=  validates the info with Plextrac's authenticate endpoints.     =",
               "=                                                                 =",
               "==================================================================="
            ]


if __name__ == '__main__':
    for i in script_info:
        print(i)

    with open("config.yaml", 'r') as f:
        args = yaml.safe_load(f)

    # Creates auth object to handle authentication, initializes with values in config
    auth = Auth(args)
    # Tries to authenticate, will use values stored or prompt the user if needed
    auth.handle_authentication()
    

    # Starting from this authentication example, you can now build out your script and call other endpoints

    # Authorization verification is built in through the get_auth_headers() method of the Auth obj
    # After the 2 lines above setting up the auth object, `auth.get_auth_headers()' will return the headers needed to add to any API calls
    print(f'\nCompleted with auth_headers: {auth.get_auth_headers()}')
