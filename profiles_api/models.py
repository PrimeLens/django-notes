from django.db import models

# AbstractBaseUser => base of the standard django user model
# permissions mixin allows us to add permissions to our user model this is important to see
# what users can have what authorization to what data
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# because we are customizing djangos user model we need to teach django how to use our new user profile model
# we do this by creating a manager object that does with out user profile model and we reference it with the line
# of code that says objects = UserProfileManager()
class UserProfileManager(BaseUserManager):
    """Helps Django work with our custom user model."""

    def create_user(self, email, name, password=None):
        """Creates a new user profile."""

        if not email:
            raise ValueError('Users must have an email address.')
        # normalize is a convert to lowercase
        email = self.normalize_email(email)
        user = self.model(email=email, name=name,)
        # set_password will encrypt to a hash that way we dont save plain text passwords
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Creates and saves a new superuser with given details."""

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user





# override djangos user model and this is called substituting a custom user model 
# the reason we do this is so we can have control over the fields we need for our system
# during the class definition we pass in AbstractBaseUser, PermissionsMixin which we inherit from
# docstring is marked by """ a brief description about what this class is for
class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represents a "user profile" inside our system"""
    email = models.EmailField(max_length=255, unique=True)
    name  = models.CharField(max_length=255)
   # this one is a requirement when you do a custom user model to django,  use it to disable user accounts
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    # this one is a requirement when you do a custom user model to django, use it for roles
    objects = UserProfileManager()
    # this is what the user will login as
    USERNAME_FIELD = 'email'
    # this is a list of fields that we decide as required from the user,  USERNAME_FIELD is in this status by default
    REQUIRED_FIELDS = ['name']
    # helper functions for our model,  put self in args because its a class function
    # I believe these are used by django admin pages
    def get_full_name(self):
        """Used to get a users full name."""
        return self.name
    def get_short_name(self):
        """Used to get a users short name."""
        return self.name
    # another required function by django when substituting  so it knows how to return our object as a string
    # this would be used when we want to print an object and know which one it is, so lets return a unique field
    def __str__(self):
        """Django uses this when it needs to convert the object to text."""
        return self.email








