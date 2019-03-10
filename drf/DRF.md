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
3. edit settings.py and add the app in to INSTALLED_APPS

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

1. copy in the serializers file from  <a href="./profiles_api/serializers.py">./profiles_api/serializers.py</a>

2. copy in the views file from  <a href="./profiles_api/views.py">./profiles_api/views.py</a>

3. copy in the permissions file from  <a href="./profiles_api/permissions.py">./profiles_api/permissions.py</a>

4. copy in the urls file from  <a href="./profiles_api/urls.py">./profiles_api/urls.py</a>

5. edit the main 'urls.py' file that is in the same folder as settings.py
- you will need to import 'include'
- add the new url path

```
from django.conf.urls import include
urlpatterns = [
    ...
    url(r'^api/', include('profiles_api.urls')),
]
```

6. in order to protect the the API root which is api/<br/>
   edit settings.py and add the following onto the end

```
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
}
```


## Test it (carefully with a temp alteration on localhost)

1. test `/api/users/` to make sure its protected
2. test `/api/` to make sure its protected

This means a token will be needed to do a GET and we will not have a token until we have a /login endpoint in the next section, so...

1. this is *temporary* for localhost only
2. go to profiles_api/views.py
3. delete IsAuthenticated from permission_classes<br/>
   `permission_classes = (IsAuthenticated, permissions.UpdateOwnProfile,)`<br/>
   `permission_classes = (permissions.UpdateOwnProfile,)`
4. verify this url works in browser http://localhost:8000/api/users/
5. change back the permission_classes before pushing to AWS

## For a continuation of auth via endpoints and an email server 
- please see private repo django-notes-auth-anu

## Summary of urls 

If the django app is at 
- https://app.mydomain.com

REST endpoint will be at 
- https://app.mydomain.com/api/

Backend Interface
- login will be https://app.mydomain.com/admin
- admin users list will be https://app.mydomain.com/admin/auth/user/
- api users list will be at https://app.mydomain.com/api/users/


