"""
Permissions for API access control.
"""
from rest_framework import permissions


SAFE_METHODS = ['HEAD', 'OPTIONS']


class IsOrgMember(permissions.BasePermission):
    """
    Check if the request user is part of the organization
    """

    def has_object_permission(self, request, view, org):
        if request.method in SAFE_METHODS:
            return True

        return org.is_member(request.user)
