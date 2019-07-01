# flaskdash
flask dash initial version

not working yet, error:

[2019-07-01 16:58:02,389] ERROR in app: Exception on / [GET]
Traceback (most recent call last):
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\app.py", line 2292, in wsgi_app
    response = self.full_dispatch_request()
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\app.py", line 1815, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\app.py", line 1718, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\_compat.py", line 35, in reraise
    raise value
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\app.py", line 1813, in full_dispatch_request
    rv = self.dispatch_request()
  File "C:\Users\sreeh\Anaconda3\lib\site-packages\flask\app.py", line 1799, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "C:\Users\sreeh\Desktop\weather_app_flask\weather_app_flask\app.py", line 53, in index_get
    validity = get_cert_validity(hostname.name)
AttributeError: 'Host' object has no attribute 'name'
127.0.0.1 - - [01/Jul/2019 16:58:02] "GET / HTTP/1.1" 500 -
