from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission class that allows owners to modify their own objects
    while allowing read-only access to others.
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user has permission to perform the given HTTP method on the object.
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user
