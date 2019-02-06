from rest_framework import serializers
from . import models

class LookoutSerializer(serializers.ModelSerializer):
    # by providing max length here we get all the error message handling
    # http://www.django-rest-framework.org/api-guide/serializers/
    # http://www.django-rest-framework.org/api-guide/fields/
    # name = serializers.CharField(max_length=10)

    class Meta:
        model = models.Lookout
        fields = ('id', 'name', 'area', 'elevation', 'climate')


