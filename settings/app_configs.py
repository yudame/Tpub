
# Users
AUTH_USER_MODEL = 'user.User'
PASSWORD_RESET_TIMEOUT_DAYS = 7
# LOGIN_URL = '/social_django/login/auth0'
# LOGIN_REDIRECT_URL = '/auth0/dashboard'


# Internationalization
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = False
USE_L10N = False
USE_TZ = True
CURRENCIES = ('THB',)


""" 
django-request is a statistics module for django. 
It stores requests in a database for admins to see, 
it can also be used to get statistics on who is online etc.
https://django-request.readthedocs.io/en/latest/settings.html#request-ignore-paths 
"""
REQUEST_IGNORE_PATHS = (
    r'^admin/',
)

# DEVELOPER TOOLS
SHELL_PLUS = "ipython"
