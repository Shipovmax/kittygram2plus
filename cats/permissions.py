from rest_framework import permissions
from rest_framework.request import Request
from rest_framework.views import APIView

from .models import Cat


class OwnerOrReadOnly(permissions.BasePermission):
    """
    Allows editing only to the object's owner.
    Everyone else (including anonymous users) gets safe methods only (GET).
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        # Allow the request if the method is safe or the user is authenticated
        return (
            request.method in permissions.SAFE_METHODS or request.user.is_authenticated
        )

    def has_object_permission(self, request: Request, view: APIView, obj: Cat) -> bool:
        # Check whether the object's owner matches the request user
        return obj.owner == request.user


class ReadOnly(permissions.BasePermission):
    """
    Allows read-only access (GET, HEAD, OPTIONS).
    """

    def has_permission(self, request: Request, view: APIView) -> bool:
        return request.method in permissions.SAFE_METHODS
