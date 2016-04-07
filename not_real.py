import requests

BASE_DOMAIN = 'not_real.com'

# PLAN: Loop over the givn args and append their values to the uri

def format_uri(kwargs):
    base_uri = 'http://' + BASE_DOMAIN + '/customer_scoring?'
    lilpieces = []
    for key, val in kwargs.iteritems():
        lilpiece = str(key) + '=' + str(val)
        lilpieces.append(lilpiece)

    # Like going through a stack of ordered pages
    # Place each one face down on the table 
    # Then flip the whole stack once finished
    lilpieces.reverse()
    # That is essentially what is going on here
    query_string = '&'.join(lilpieces)
    formatted_uri = base_uri + query_string
    return formatted_uri

def key_up_args(args):
    # Provide default values for un specified keys
    default_args = ['income','zipcode','age']
    sliced_args = default_args[:len(args)]
    keyed_args = dict(zip(sliced_args, args))
    return keyed_args

def get_customer_scoring(*args, **kwargs):
    if len(args) < 1 and len(kwargs) < 1:
        # Throws error message
        print('ERROR not_real.get_customer_scoring() requires minimum one argument')
        return None
    elif len(kwargs) > 0:
        # let keyword arguments override plain args
        uri = format_uri(kwargs)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()
    else: 
        extra_args = map(lambda x: str(x), args[3:]) if len(args) > 3 else False
        if extra_args != False:
            message = 'WARNING ' + ', '.join(extra_args) +\
                    ' were omitted, max 3 parameters allowed'
            print(message)
        keyed_args = key_up_args(args[:3])
        print("##########"+"keyedarrgs")
        print(keyed_args)
        uri = format_uri(keyed_args) 
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

