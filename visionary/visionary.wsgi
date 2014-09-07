import os
import sys
import site


sys.path.append('/home/ray/projects/Sup/visionary')
sys.path.append('/home/ray/projects/Sup/visionary')
site.addsitedir('/home/ray/projects/Sup/visionary/venv/lib/python3.4/site-packages')

os.environ['PYTHON_EGG_CACHE'] = '/home/ray/projects/Sup/visionary/.python-egg'
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()

# import os
# import sys

# sys.path.append('/var/www/ducklington.org/application')

# os.environ['PYTHON_EGG_CACHE'] = '/var/www/ducklington.org/.python-egg'

# def application(environ, start_response):
#     status = '200 OK'
#     output = 'Hello World!'
# 
#     response_headers = [('Content-type', 'text/plain'),
#                         ('Content-Length', str(len(output)))]
#     start_response(status, response_headers)
# 
#     return [output]