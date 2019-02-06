from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views
router = DefaultRouter()
# first param is the api path
# base_name param is the code class name more about it here 
# https://stackoverflow.com/a/50382141  and   https://stackoverflow.com/a/22114793
router.register('lookout', views.LookoutViewSet, base_name='lookout')
urlpatterns = [
    url(r'', include(router.urls)),
]
