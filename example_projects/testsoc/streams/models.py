from django.db import models

class Post(models.Model):
  user_id = models.PositiveIntegerField(default=0)
  link_or_text = models.CharField(max_length=4)
  title = models.CharField(max_length=200)
  body = models.TextField(blank=True, null=True, default='')
  linkout = models.CharField(max_length=200, blank=True, null=True, default='')
  num_of_replies = models.PositiveIntegerField(default=0)