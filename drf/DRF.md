

## (optional) VirtualBox and Vagrant

- get virtualbox from virtualbox.org
- get vagrant from vagrantup.com
  after install type `vagrant version` to check it is installed
- do `vagrant init` when in the project folder
- get a vagrant file from the course from here https://gist.github.com/LondonAppDev/d990ab5354673582c35df1ee277d6c24



## DRF

- `pip install djangorestframework==3.7.7`
- go to settings.py and add `rest_framework` and `rest_framework.authtoken`


```
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
]
```

## Save the required python libraries

`pip freeze > requirements.txt`

## Create a custom user model to override django's user model
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
admin.site.register(models.UserProfile)
```
6. do `python manage.py createsuperuser`<br/>
```
    Email: aaa@aaa.com<br/>
    Name: aaa<br/>
    Password: Awesome1<br/>
```
7. do `python manage.py runserver` and test it by login in at /admin


## APIView
in edit main app `djangomyproj/urls.py` paste or merge in
```
from django.conf.urls import include
urlpatterns = [
    # the ^ means anything that starts with
    # https://docs.djangoproject.com/en/1.11/topics/http/urls/
    # 'profiles_api.urls' means go to profiles_api django app and 
    # include the urls .py file from there
    url(r'^wat/', include('profiles_api.urls')),
]
```
create profiles_api > urls.py 
```
from django.conf.urls import url
from . import views
urlpatterns = [
    # this url param matches after the one in the main urls.py so in this case it would be /wat/moo/
    url(r'^moo/', views.HelloApiView.as_view()),
]
```

in profiles_api > views.py paste
```
from rest_framework.views import APIView
from rest_framework.response import Response

class HelloApiView(APIView):
    def get(self, request, format=None):
        some_data= [
            'low',
            'remmy',
            'iinterleccy property',
            'dolores',
        ]
        return Response({'wat': some_data})
```

- Test the GET from the browser which will contain a header accept text/html and django will detect that and send the browser a nicely formatted page
- Test the GET from insomnia or postman and the response header will state type json and a body of json will be present as above 

## Serializers convert text string of json to a python object and vice versa

create profiles_api > serializers.py

```
from rest_framework import serializers
class HelloSerializer(serializers.Serializer):
    # by providing max length here we get all the error message handling
    # http://www.django-rest-framework.org/api-guide/serializers/
    # http://www.django-rest-framework.org/api-guide/fields/
    name = serializers.CharField(max_length=10)
```
in profiles_api > views.py paste
```
# for the serializer line below, this is guard rails for user input
from . import serializers
from rest_framework import status
# the next part goes immediately after class HelloApiView
    serializer_class = serializers.HelloSerializer
# then add a function at the end but within HelloApiView
    def post(self, request):
        serializer = serializers.HelloSerializer(data=request.data)
        if serializer.is_valid():
            # this just sends back a hello message
            name = serializer.data.get('name')
            message = 'Hello {0}!'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```






