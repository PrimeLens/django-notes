

## viewsets

1. Create the lookoutapp `python manage.py startapp lookoutapp`
2. create a model

```
from django.db import models
class Lookout(models.Model):
    name = models.CharField(max_length=200)
    area = models.TextField(blank=True)
    elevation = models.IntegerField(blank=True, default=0)
    climate = models.CharField(max_length=200, blank=True)
```

3. run migrations so there is a table in the DB (otherwise /admin will crash)

```
python manage.py makemigrations
python manage.py migrate
```

4. create admin.py

```
from django.contrib import admin
from .models import Lookout 
class LookoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'area', 'elevation', 'climate']
admin.site.register(Lookout, LookoutAdmin)
```

5. in the main app urls.py edit to add in

```
from django.conf.urls import include
urlpatterns = [
    ...
    url(r'^api/v2/', include('lookoutapp.urls')),
]
```

6. create `lookoutapp/urls.py` and add the following which automatically creates routes<br/>
note: you will have a main index page of all the routes

```
from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
# first param is the api path
# base_name param is the code class name more about it here 
# https://stackoverflow.com/a/50382141  and   https://stackoverflow.com/a/22114793
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')
urlpatterns = [
    url(r'', include(router.urls)),
]
```

7.  next you will need to choose between a few options

<hr/>

## Option 1: Extending classes serializers.ModelSerializer and viewsets.ModelViewSet
- taken from https://wsvincent.com/django-rest-framework-serializers-viewsets-routers/
- `/api/v2/lookout/` and `/api/v2/lookout/1/`

serializers.py
```
from rest_framework import serializers
from . import models
class LookoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lookout
        fields = ('id', 'name', 'area', 'elevation', 'climate')
```
views.py
```
from rest_framework import viewsets
from . import serializers
from . import models
class LookoutViewSet(viewsets.ModelViewSet):
    queryset = models.Lookout.objects.all()
    serializer_class = serializers.LookoutSerializer
```
<hr/>

## Option 2: Extending classes serializers.Serialize and viewsets.ViewSet
- this example was given by mark in the udemy course
- there will be no link to get to the instance so put `/1` at the end of the url
- `/api/v2/lookout/` and `/api/v2/lookout/1/`
- will use the serializer to error check the input to 10 characters

serializers.py

```
from rest_framework import serializers

class LookoutSerializer(serializers.Serializer):
    # by providing max length here we get all the error message handling
    name = serializers.CharField(max_length=10)
    # http://www.django-rest-framework.org/api-guide/serializers/
    # http://www.django-rest-framework.org/api-guide/fields/
```

views.py

```
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from . import serializers

class LookoutViewSet(viewsets.ViewSet):
    serializer_class = serializers.LookoutSerializer
    def list(self, request):
        a_viewset = ['a', 'b', 'c']
        return Response({'message': 'Hello!', 'a_viewset': a_viewset})

    def create(self, request):
        serializer = serializers.LookoutSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.data.get('name')
            message = 'Hello {0}'.format(name)
            return Response({'message': message})
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        return Response({'http_method': 'GET'})

    def update(self, request, pk=None):
        return Response({'http_method': 'PUT'})

    def partial_update(self, request, pk=None):
        return Response({'http_method': 'PATCH'})

    def destroy(self, request, pk=None):
        return Response({'http_method': 'DELETE'})
```



