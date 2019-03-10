from rest_framework import viewsets
from . import serializers
from . import models
# the following two are together
from . import permissions
from rest_framework.authentication import TokenAuthentication

from rest_framework.authtoken.views import ObtainAuthToken

from rest_framework.permissions import IsAuthenticated


class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()

    # the trailing comma is important in order to type this as a tuple
    # the reason these are tuples is you may want to use multiple types of authentication
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, permissions.UpdateOwnProfile,)


