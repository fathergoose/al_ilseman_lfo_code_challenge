import requests

BASE_DOMAIN = 'not_real.com'
path = 'http://' + BASE_DOMAIN + '/customer_scoring'


def format_uri(kwargs):


    base_uri = 'http://' + BASE_DOMAIN + '/customer_scoring?'
    lilpieces = []
    for key, val in kwargs.iteritems():
        lilpiece = str(key) + '=' + str(val)
        lilpieces.append(lilpiece)
    lilpieces.reverse()
    query_string = '&'.join(lilpieces)
    formatted_uri = base_uri + query_string
    return formatted_uri


def key_up_args(args):


    default_args = ['income','zipcode','age']
    sliced_args = default_args[:len(args)]
    keyed_args = dict(zip(sliced_args, args))
    return keyed_args


def submit_request(cust_info):


    try:
        response = requests.get(path, params=cust_info)
        if not response.status_code // 100 == 2:
            return 'ERROR: The server returned {}'.format(response)
        else:
            return response.json()
    except requests.exceptions.RequestException as err:
        return 'ERROR: {}'.format(err)
        sys.exit(1)


def get_customer_scoring(*args, **kwargs):


    if len(args) < 1 and len(kwargs) < 1:
        print('ERROR not_real.get_customer_scoring() requires minimum one argument')
        return None
    elif len(kwargs) > 0:
        #uri = format_uri(kwargs)
        response = submit_request(kwargs)
        return response
    elif type(args[0]) is dict:
        #uri = format_uri(args[0])
        response = submit_request(args[0])
        return response
    else: 
        if len(args) > 3:
            extra_args = map(lambda x: str(x), args[3:]) 
            message = 'WARNING ' + ', '.join(extra_args) +\
                      ' were omitted, max 3 parameters allowed'
            print(message)
        keyed_args = key_up_args(args[:3])
        # uri = format_uri(keyed_args) 
        response = submit_request(keyed_args)
        return response
