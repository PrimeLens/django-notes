
from rest_framework import viewsets
from . import serializers
from . import models

class LookoutViewSet(viewsets.ModelViewSet):
    queryset = models.Lookout.objects.all()
    serializer_class = serializers.LookoutSerializer


