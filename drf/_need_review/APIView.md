


## APIView a simple GET
in edit main app `djangomyproj/urls.py` paste or merge in
```
from django.conf.urls import include
urlpatterns = [
    # the ^ means anything that starts with
    # https://docs.djangoproject.com/en/1.11/topics/http/urls/
    # 'myfirstapp.urls' means go to myfirstapp django app and 
    # include the urls .py file from there
    url(r'^apiview/', include('myfirstapp.urls')), 
    # it is possible to have another line with the same regex and it gets appended
]
```

create `myfirstapp/urls.py` 
```
from django.conf.urls import url
from . import views
urlpatterns = [
    # this url param matches after the one in the main urls.py so in this case it would be /apiview/items/
    url(r'^items/$', views.ItemsApiView.as_view()),
    url(r'^items/(?P<item_id>\w+)/$', views.ItemsApiView.as_view()),
]
```

in `myfirstapp/views.py` paste
```
from rest_framework.views import APIView
from rest_framework.response import Response

# for the serializer line below, this is guard rails for user input
from . import serializers
from rest_framework import status

# import the models for gettting DB data
from . import models
from django.http import Http404

class ItemsApiView(APIView):

    serializer_class = serializers.ItemSerializer

    def get(self, request, item_id=None):
        if item_id:
            try:
                ItemQueryObj = models.Item.objects.get(id=item_id)
            except models.Item.DoesNotExist:
                raise Http404
            # convert python object to a dict(?)
            serializedItems = self.serializer_class(ItemQueryObj)
        else:
            itemsQuerySet = models.Item.objects.all()
            # convert python object to a collection (also known as ordered dict)
            serializedItems = self.serializer_class(itemsQuerySet, many=True)
        # itemsQuerySet = models.Item.objects.all()
        # itemsQuerySet = models.Item.objects.all()[0].__dict__
        # itemsQuerySet = models.Item.objects.get(id=1)
        # itemsQuerySet = models.Item.objects.filter(email='aaa@aaa.com')
        return Response(serializedItems.data)

```

Serializers convert text string of json to a python object and vice versa

in `myfirstapp/serializers.py` paste
```
from rest_framework import serializers
from . import models

class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Item
        # you must specfy all the fields
        # https://www.django-rest-framework.org/api-guide/serializers/#specifying-which-fields-to-include
        fields = "__all__"
```

- Kick over the server (in case it has crashed) with `python manage.py runserver`
- use admin to make sure items are added into the DB
- Test the GET from the browser `http://127.0.0.1:8000/apiview/items/`
- Test the GET from the browser `http://127.0.0.1:8000/apiview/items/1`
- The GET contains a header of accept text/html and django will detect that and send the browser a nicely formatted page
- Test the GET from insomnia or postman and the response header will state type json and a body of json will be present as above 

## POST, PUT, PATCH, DELETE

in `myfirstapp/views.py` edit in the following
```
    def post(self, request, item_id=None):
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            r = Response(serializer.validated_data)
        else:
            r = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return r

    # used to replace ALL fields of a record at this ID
    def put(self, request, item_id=None):
        try:
            ItemQueryObj = models.Item.objects.get(id=item_id)
        except models.Item.DoesNotExist:
            raise Http404
        # TO DO - to really spearate PUT from PATCH the serialize should fill in the missing fields with defaults but there is little use for PUT 
        serializer = serializers.ItemSerializer(data=request.data)
        if serializer.is_valid():
            # https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py#L969
            serializer.update(ItemQueryObj, serializer.validated_data)
            r = Response(status=status.HTTP_202_ACCEPTED)
        else:
            r = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return r


    # used to replace some fields of a record at this ID
    def patch(self, request, item_id=None):
        try:
            ItemQueryObj = models.Item.objects.get(id=item_id)
        except models.Item.DoesNotExist:
            raise Http404
        serializer = serializers.ItemSerializer(data=request.data, partial=True)
        if serializer.is_valid():
            # https://github.com/encode/django-rest-framework/blob/master/rest_framework/serializers.py#L969
            serializer.update(ItemQueryObj, serializer.validated_data)
            r = Response(status=status.HTTP_202_ACCEPTED)
        else:
            r = Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return r

    # used to delete record at this ID
    def delete(self, request, item_id=None):
        try:
            ItemQueryObj = models.Item.objects.get(id=item_id)
        except models.Item.DoesNotExist:
            raise Http404
        ItemQueryObj.delete();
        return Response(status=status.HTTP_410_GONE)

```



