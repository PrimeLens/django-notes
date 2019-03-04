This folder of notes needs review.<br/>
A working app has been dropped in here as a temporary replacement.

- copy folder (/example_lookout_app) into code
- add the app in the settings.py

- fire up the virtual env with `source bin/activate`
- above the src folder do `pip install djangorestframework==3.7.7` to add to our virtual environment
- go to settings.py and add `rest_framework` and `rest_framework.authtoken`

```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

- Cors needs to be added https://pypi.org/project/django-cors-headers/<br/>
  `pip install django-cors-headers`<br/>

```
INSTALLED_APPS = [
    ...
    'corsheaders',
]
MIDDLEWARE = [
    # must go at start !!
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    ...
]
# https://pypi.org/project/django-cors-headers/
CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?ferryman\.com$', )
# CORS_ORIGIN_WHITELIST = (
#     'localhost:3003',
# )
```

- edit ALLOWED_HOSTS<br/>
  `ALLOWED_HOSTS = ['localhost', '.ferryman.com', '.rarespirits.com', '.elasticbeanstalk.com']`
- `pip freeze > requirements.txt`
- eb deploy (env name)


## URLS 

If the django app is at 
- https://app.mydomain.com

REST endpoint will be at 
- https://app.mydomain.com/api/v2/

Backend Interface
- login will be https://app.mydomain.com/admin
- users list will be https://app.mydomain.com/admin/auth/user/
- lookouts list will be https://app.mydomain.com/admin/lookout/lookout/

## Create the profile API
- from the command line enter the shell<br/>
  `source ../bin/activate`
- `python manage.py startapp profiles_api`
- copy in the models file from  <a href="./profiles_api/models.py">./profiles_api/models.py</a>

## For a continuation of auth via endpoints and an email server 
- please see private repo aws-notes/aws django/aws_django_auth_anu.md



## Protecting the endpoint from unauthorized access

Edit `lookout/views.py` and add

```
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
```

and into the start of the function ahead of the query

```
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
```

You will now need the correct header on the request

