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
    # And now I see that all this param parsing can be done with requests :(
    query_string = '&'.join(lilpieces)
    formatted_uri = base_uri + query_string
    return formatted_uri

def key_up_args(args):
    # Provide default values for un specified keys
    default_args = ['income','zipcode','age']
    sliced_args = default_args[:len(args)]
    keyed_args = dict(zip(sliced_args, args))
    return keyed_args

def submit_request(uri):
    try:
        response = requests.get(uri)
        if not response.status_code // 100 == 2: # floor divide to make sure it's a 2xx response
            return 'ERROR: The server returned {}'.format(response)
        else:
            return response.json()
    except requests.exceptions.RequestException as err:
        return 'ERROR: {}'.format(err)
        sys.exit(1) # Something is way wrong

def get_customer_scoring(*args, **kwargs):
    if len(args) < 1 and len(kwargs) < 1:
        # Throws error message
        print('ERROR not_real.get_customer_scoring() requires minimum one argument')
        return None
    elif len(kwargs) > 0:
        # let keyword arguments override plain args
        uri = format_uri(kwargs)
        response = submit_request(uri)
        return response
            
    elif type(args[0]) is dict:
        # allow a dict of options too
        uri = format_uri(args[0])
        response = submit_request(uri)
        return response
    else: 
        # construct error message from extra arguments
        extra_args = map(lambda x: str(x), args[3:]) if len(args) > 3 else False
        if extra_args != False:
            message = 'WARNING ' + ', '.join(extra_args) +\
                    ' were omitted, max 3 parameters allowed'
            print(message)
        keyed_args = key_up_args(args[:3])
        uri = format_uri(keyed_args) 
        response = submit_request(uri)
        return response

