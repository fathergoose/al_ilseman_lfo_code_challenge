# Original Documentation

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

# Revisions

*How would you better handle bad input from your users?*
I have included the ability for `get_customer_scoring()` to accept keyword arguments, a dictionary of arguments, and have included also included an interactive script so the program could be used stand alone. It was difficult to decide how to restrict the users input without understanding anything about the server and it's limitations.

*How would you be more clear about errors (user errors, internal errors, server errors)*
The old version of the program had two types of errors, `print()` errors I wrote and exceptions which would crash the client. The server / web responses are now handled more gracefully with a try/except block and only 'dangerous' errors stop things. Non 2xx response codes are considered a non-dangerous error and the status codes are now passed along in lieu of a response.

*How would you simplify the usage of your client?*
I looked into making a GUI, but decided that in the amount of time I had it would be more copy pasting than understanding. Insted, I went with an interactive script. It's far from fancy, but it illustrates the point.
```
./interact
```
This will start the script and loops until the user decides he/she is finished. In addition to the script, I also made `get_customer_scoring()` more flexible in the types of inputs it is willing to accept. The key here is **more** flexible, it still accepts all input as before and all of the old tests still pass, but now there are more options.

*How would you make your code less verbose/more DRY?*
Tried to move all of the fancy logic into separate functions. Allowing `get_customer_scoring()` to be about high level logic and control flow. I also realized, very late, that the requests library can handle much of the url parameter construction for me. Knowing this, `not_real.py` could be simplified to no longer include my own, buggy url constructions.

*How would you better handle bad responses from the server?*
See above. Bad server requests are now just passed allong more similarly to a regular response allowing the user to see the resoponse code and keep going.

*How would you package your client up for installation via PyPI?*
I packaged the module and published it to https://testpypi.python.org/pypi. It is available under the name `not_real`.
```
pip install -i https://testpypi.python.org/pypi not_real
```
To avoid polluting of the real PyPI, I have published my module to the PyPI test server. I did this following the instructions found [here](https://wiki.python.org/moin/TestPyPI) among other places.

*How would you handle automatic installation of requirements (preferably in a way that doesn’t pollute your core language environment)?*
Virtualenv is a python tool to allow for just such requirements. After installing virtualenv with pip, it can be initialized like so:
```
virtualenv ENV --no-site-packages --verbose
```

Now that virtualenv is installed in initialized one is able to `source ENV/bin/activate` and let virtualenv take over our shell. This will intercept calls to any python related executables and redirect them to the versions found inside the `ENV` directory. Also, anything we install with pip will also be put under `ENV`. This means we can run the install command from the previous question and my silly little module will be placed in it's own little sandbox under `ENV/`.
