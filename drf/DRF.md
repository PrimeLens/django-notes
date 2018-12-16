

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

## Using a viewset to continue our profiles API

1. in the main app > urls.py add the line<br/>
`url(r'^api/', include('profiles_api.urls')),`
2. create profiles_api > urls.py and add the following code

```
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
# because UserProfileViewSet inherits from viewsets.ModelViewSet it automatically figures out base_name
# the string 'profile' will be in the path but because the main app urls.py is first it is /api/profile/
router.register('profile', views.UserProfileViewSet)
urlpatterns = [
    url(r'', include(router.urls))
]
```

3. create profiles_api > views.py and add the following code

```
from rest_framework import viewsets
from . import serializers
from . import models
# the following two are together
from . import permissions
from rest_framework.authentication import TokenAuthentication

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""
    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()
    # the trailing comma is important in order to type this as a tuple
    # the reason these are tuples is you may want to use multiple types of authentication
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
```

4. create profiles_api > serializers.py and add the following code 

```
from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_active')
        # define extra key word arguments for our model
        # special attributes that are predefined in the docs, get applied to password
        # write only is set because then the API will not return the password in the GET
        extra_kwargs = {'password': {'write_only': True}}

    # this create over-rides the existing 'create' provided by serializers.ModelSerializer
    def create(self, validated_data):
        """Create and return a new user."""
        # creates a new user model
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        # I think this is where the hashing takes place
        user.set_password(validated_data['password'])
        user.save()
        return user
```

5. create profiles_api > permissions.py and add the following code

```
from rest_framework import permissions
# https://www.django-rest-framework.org/api-guide/permissions/ 

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""
    # this function is called every time there is a request to our API
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        # if user just wants to view (GET is safe method) then we return True
        if request.method in permissions.SAFE_METHODS:
            return True
        # this allows someone to edit or delete their own account, # but what about admin editing anothers account?
        return obj.id == request.user.id
```

## Login API (and nesting an APIView in a viewset)

DRF has a login API out-of-the box but it is APIView not a viewset however we can trick it so it still works with the DefaultRouter. We do this by creating a viewset that passes the request through to the ObtainAuthToken APIView

edit `profiles_api/urls.py` and add 

```
# now register the login API we are creating setting the base_name because its not a ModelViewSet
router.register('login', views.LoginViewSet, base_name='login')
```

edit `profiles_api/views.py` and add 

```
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class LoginViewSet(viewsets.ViewSet):
    """Checks email and password and returns an auth token"""
    serializer_class = AuthTokenSerializer
    # replace the default create method
    def create(self, request):
        """Use the ObtainAuthToken APIView to validate and create a token"""
        # call the post function of a new APIView instance and pass it the request, this will return a new token
        return ObtainAuthToken().post(request)
```

Note that when viewing this in the Django rest browser interface you will see the following and thats because you cannot call a GET on the login API only a POST

<img alt="" src="../images/7.png" width="518"/>








