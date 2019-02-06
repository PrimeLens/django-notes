from django.db import models


from django.db import models
class Lookout(models.Model):
    name = models.CharField(max_length=200)
    area = models.TextField(blank=True)
    elevation = models.IntegerField(blank=True, default=0)
    climate = models.CharField(max_length=200, blank=True)
