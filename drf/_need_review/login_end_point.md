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