import requests

BASE_DOMAIN = 'not_real.com'

# PLAN: Loop over the givn args and append their values to the uri

def format_uri(**kwargs):
    base_uri = 'http://' + BASE_DOMAIN + '/customer_scoring?'
    print(base_uri)
    parameters = sorted(kwargs.keys())
    for param in parameters:
        lilpiece = param + '=' + kwargs[param]
        lilpieces = []
        lilpieces.append(lilpiece)

    query_string = '&'.join(lilpieces)
    formatted_uri = base_uri + query_string
    return formatted_uri

def get_customer_scoring(*args):

    if len(args) < 1:
        print('ERROR not_real.get_customer_scoring() requires minimum one argument')
        return None

    if len(args) == 1:
        uri = 'http://{0}/customer_scoring?income={1}'\
        .format(BASE_DOMAIN, args[0])
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) == 2:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}'\
        .format(BASE_DOMAIN, args[0], args[1])
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) == 3:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}&age={3}'\
        .format(BASE_DOMAIN, args[0], args[1], args[2])
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) > 3:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}&age={3}'\
        .format(BASE_DOMAIN, args[0], args[1], args[2])
        extra_args = map(lambda x: str(x), args[3:])
        message = 'WARNING ' + ', '.join(extra_args) +\
                ' were omitted, max 3 parameters allowed'
        print(message)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

