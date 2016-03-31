import requests

BASE_DOMAIN = 'not_real.com'

def get_customer_scoring(*args):

    if len(args) < 1:
        print('ERROR not_real.get_customer_scoring() requires minimum one argument')

    if len(args) == 1:
        uri = 'http://{0}/customer_scoring?income={1}'\
        .format(BASE_DOMAIN, args[0])
        print(uri)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) == 2:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}'\
        .format(BASE_DOMAIN, args[0], args[1])
        print(uri)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) == 3:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}&age={3}'\
        .format(BASE_DOMAIN, args[0], args[1], args[2])
        print(uri)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

    if len(args) > 3:
        uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}&age={3}'\
        .format(BASE_DOMAIN, args[0], args[1], args[2])
        print(uri)
        extra_args = map(lambda x: str(x), args[3:])
        message = 'WARNING ' + ', '.join(extra_args) +\
                ' were omitted, max 3 parameters allowed'
        print(message)
        response = requests.get(uri)
        response.raise_for_status()
        return response.json()

