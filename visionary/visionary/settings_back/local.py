from .base import *


DEBUG = True
TEMPLATE_DEBUG = DEBUG

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.request',
    'django.core.context_processors.static',    
)


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
  	'NAME': get_env_variable("DATABASE_NAME"),
        'USER': get_env_variable("DATABASE_USER"),
        'PASSWORD': get_env_variable("DATABASE_PASSWORD"),
        'HOST': 'localhost',
        'PORT': '',
    }
}

