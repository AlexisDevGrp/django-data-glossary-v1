from .base import *

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST ='smtp.mailtrap.io'
EMAIL_HOST_USER ='9970a6ff348c23'
EMAIL_HOST_PASSWORD ='1a0aa24a966cc6'
EMAIL_PORT ='2525'
DOMAIN='localhost:8000'
DEFAULT_FROM_EMAIL = 'alexisdevgrp@gmail.com'
DOMAIN = 'CDL'
SITE_NAME = 'CDL Business Object Gloassary'

DATABASES = {
    "default": {
        "ENGINE": env("POSTGRES_ENGINE"),
        "NAME": env("POSTGRES_DB"),
        "USER": env("POSTGRES_USER"),
        "PASSWORD": env("POSTGRES_PASSWORD"),
        "HOST": env("PG_HOST"),
        "PORT": env("PG_PORT"),
    }
}
