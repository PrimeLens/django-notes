from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """A serializer for our user profile objects."""

    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password', 'is_active')
        # define extra key word arguments for our model
        # special attributes that are predefined in the docs, get applied to password
        # write only is set because then the API will not return the password in the GET
        extra_kwargs = {'password': {'write_only': True}}

    # this create over-rides the existing 'create' provided by serializers.ModelSerializer
    def create(self, validated_data):
        """Create and return a new user."""
        # creates a new user model
        user = models.UserProfile(
            email=validated_data['email'],
            name=validated_data['name']
        )
        # where the hashing takes place
        user.set_password(validated_data['password'])
        user.save()
        return user

