from httmock import response, urlmatch

NETLOC = r'(.*\.)?not_real\.com$'
HEADERS = {'content-type': 'application/json'}

@urlmatch(
        netloc=NETLOC,
        path='/customer_scoring',
        method='get',
        query=r'^income=\d+\&zipcode=\d+\&age=\d'
        )
def customer_scoring_query_mock(self, url, request):
    return {'propensity': 0.26532, 'ranking': 'C'}
