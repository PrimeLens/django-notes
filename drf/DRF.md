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


## Create the profile API
1. from the command line enter the shell<br/>
  `source ../bin/activate`
2. `python manage.py startapp profiles_api`
3. add the app in to INSTALLED_APPS

```
INSTALLED_APPS = [
    ...
    # for custom users
    'profiles_api',
]
```

4. copy in the models file from  <a href="./profiles_api/models.py">./profiles_api/models.py</a>
5. add this to the end of settings

```
# custom user model to override django's user model for DRF
AUTH_USER_MODEL = 'profiles_api.UserProfile'
```

6. Now you can do

```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

7. creating the superuser will mean that the email is provided as the username

8. edit profiles_api/admin.py file

```
from . import models
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active', 'is_staff']

# register the user admin
admin.site.register(models.UserProfile, UserAdmin)
```

## Test it

test it by checking `http://localhost:8000/admin/` and going into User profiles

## A protected endpoint to read/update user profiles



## For a continuation of auth via endpoints and an email server 
- please see private repo django-notes-auth-anu


<hr/>
<hr/>
<hr/>



## FIX - URLS 

If the django app is at 
- https://app.mydomain.com

REST endpoint will be at 
- https://app.mydomain.com/api/v2/

Backend Interface
- login will be https://app.mydomain.com/admin
- users list will be https://app.mydomain.com/admin/auth/user/
- lookouts list will be https://app.mydomain.com/admin/lookout/lookout/



## FIX - Protecting the endpoint from unauthorized access

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

