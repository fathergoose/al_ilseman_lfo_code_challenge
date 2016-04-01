Version: Python 2.7.10
Dependencies: 
    httmock==1.2.5
    requests==2.7.0

## Useage

This library consists of a single function `get_customer_scoring(income, zipcode, age)`. This function takes up to three arguments: income, zipcode, and age. These parameters are used to construct a url of the form 

```
http://not_real.com/customer_scoring?income=60000
http://not_real.com/customer_scoring?income=60000&zipcode=60626
http://not_real.com/customer_scoring?income=60000&zipcode=60626&age=27
```
depending on whether 1, 2, or 3 parameters are passed.

## Testing

`python test_not_real.py` will run the test suite. The httmock library is being used to provide mock api endpoint responses. This mock api is designed to match querries with 1 to 3 parameters and provide a response of `{'propensity': 1.26532, 'ranking': 'C'}` regardless of the query.

## Bonus

I made a minimal sinatra service to respond to the library as well. I got it woking by putting 'not_real.com' in my /etc/hosts file pointing back to localhost, then use nginx to pass between ports 80 and 4567.
