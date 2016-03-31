import requests

BASE_DOMAIN = 'not_real.com'

def get_customer_scoring(income, zipcode, age):
    uri = 'http://{0}/customer_scoring?income={1}&zipcode={2}&age={3}'\
    .format(BASE_DOMAIN, income, zipcode, age)
    print(uri)
    response = requests.get(uri)
    response.raise_for_status()
    return response.json()

