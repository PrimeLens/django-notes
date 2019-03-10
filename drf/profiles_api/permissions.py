from rest_framework import permissions
# https://www.django-rest-framework.org/api-guide/permissions/ 

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile."""

    # this function is called every time there is a request to our API
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile."""
        # if user just wants to view (GET is safe method) then we return True
        if request.method in permissions.SAFE_METHODS:
            return True
        # this allows someone to edit or delete their own account, # but what about admin editing anothers account?
        return obj.id == request.user.id

