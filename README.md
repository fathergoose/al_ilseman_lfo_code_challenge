Version: Python 2.7.10
Dependencies: 
    httmock==1.2.5
    requests==2.7.0

## Useage

This library consists of a single function `get_customer_scoring()`. This function takes three arguments: income, zipcode, and age. These parameters are used to construct a url of the form 
```
http://not_real.com/customer_scoring?income=60000&zipcode=60626&age=27
```
