from .settings import *

# Database

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME' : 'blogdb',
        'USER' : "root",
        'PASSWORD' : "carlitos1",
        'HOST' : 'localhost',
        'PORT' : 3306,
    }
}