

## (optional) VirtualBox and Vagrant

- get virtualbox from virtualbox.org
- get vagrant from vagrantup.com
  after install type `vagrant version` to check it is installed
- do `vagrant init` when in the project folder
- get a vagrant file from the course from here https://gist.github.com/LondonAppDev/d990ab5354673582c35df1ee277d6c24



## DRF

- above the src folder do `pip install djangorestframework==3.7.7` to add to our virtual environment
- fire up the virtual env with `source bin/activate`
- go to settings.py and add `rest_framework` and `rest_framework.authtoken`


```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

## Save the required python libraries

Almost forgot, its a good idea to list the libs and pipe to a text file.<br/>
Do this inside `/src` so it is included in git.<br/>
Command is this `pip freeze > requirements.txt`

## Create a custom user model to override django's user model
We do this so that the username field during login is the users email and it is treated as unique
1. create a django app called profiles_api<br/>
   `python manage.py startapp profiles_api`<br/>
   add `'profiles_api'` into app `INSTALLED_APPS = [...]`
2. edit the new app `profiles_api/models.py` and use [this code](../profiles_api/models.py) 
3. edit main app `djangomyproj/settings.py` and add a new line at the bottom 
    `AUTH_USER_MODEL = 'profiles_api.UserProfile'`
4. do `python manage.py makemigrations` and `python manage.py migrate` as per my main notes
5. edit the new app `profiles_api/admin.py` 

```
from . import models
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'is_active', 'is_staff']
admin.site.register(models.UserProfile, UserAdmin)
```

6. do `python manage.py createsuperuser`<br/>
```
    Email: aaa@aaa.com<br/>
    Name: aaa<br/>
    Password: Awesome1<br/>
```
7. do `python manage.py runserver` and test it by login in at /admin

## APIViews

[For APIViews go here LINK](./APIView.md)

## viewsets

[For viewsets go here LINK](./viewsets.md)











