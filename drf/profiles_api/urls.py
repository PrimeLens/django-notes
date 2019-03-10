from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

# because UserProfileViewSet inherits from viewsets.ModelViewSet it automatically figures out base_name
# the string 'users' will be in the path but because the main app urls.py is first it is /api/users/
router.register('users', views.UserProfileViewSet)

urlpatterns = [
    url(r'', include(router.urls))
]

