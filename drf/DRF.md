This folder of notes needs review.<br/>
A working app has been dropped in here as a temporary replacement.

- copy folder into code
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
  `CORS_ORIGIN_REGEX_WHITELIST = (r'^(https?://)?(\w+\.)?ferryworth\.com$', )`
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


## Login Endpoint

urls.py (can be any app that seems logical)

```
from rest_framework.routers import DefaultRouter
from .views import LoginViewSet
router = DefaultRouter()
router.register('login', LoginViewSet, base_name='login')

urlpatterns = [
    ...
    url(r'^api/', include(router.urls)),
]
```


views.py

```
from rest_framework import viewsets
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

Now you can 
- make a POST request to `http://localhost:8000/api/login/`
- Header: 
  - Content-Type: multipart/form-data
- Formdata: 
  - username: aaa
  - password: 123456


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
