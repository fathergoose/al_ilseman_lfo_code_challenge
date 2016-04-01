## Requirements
This library was build an run using python 2.7.10 and makes use of httmock==1.2.5 and requests==2.7.0. 
    
    

## Useage

This library consists of a single function `get_customer_scoring(income, zipcode, age)`. This function takes up to three arguments: income, zipcode, and age. These parameters are used to construct a url of the form 

```
http://not_real.com/customer_scoring?income=60000
http://not_real.com/customer_scoring?income=60000&zipcode=60626
http://not_real.com/customer_scoring?income=60000&zipcode=60626&age=27
```
depending on whether 1, 2, or 3 parameters are passed.

## Testing

`python test_not_real.py` run from the project root will execute the test suite. The httmock library is being used to provide mock api endpoint responses. This mock api is designed to match queries with 1 to 3 parameters and provide a response of `{'propensity': 1.26532, 'ranking': 'C'}` regardless of the query.

## Bonus

I made a minimal sinatra service to respond to the library as well. I got it working by putting 'not_real.com' in my /etc/hosts file pointing back to localhost, 
```
# echo '127.0.0.1 not_real.com' >> /etc/hosts
```

then use nginx to pass between ports 80 and 4567 by linking nginx-proxy into `sites-enabled`.
```
# ln -s nginx-proxy /etc/nginx/sites-enabled/
```

It would have made sense to use flask as opposed to sinatra, but I'm more fluent with ruby and it was mostly just for fun.

### Use the bonus

The bonus com.rb assumes the gems sinatra 1.4.7, thin 1.6.4, and json 1.8.3 installed as well as ruby 2.2.3. The web server is an executable so just `./com.rb` and it should fire up. 
