"""
Permissions for Organization API
"""
from rest_framework import permissions

from organizations import constants


SAFE_METHODS = ['HEAD', 'OPTIONS', 'GET']
OWNER_METHODS = ['PATCH']


class OrgPermissions(permissions.BasePermission):
    """
    Check if the request user is part of the organization or owner
    """

    def has_object_permission(self, request, view, org):
        if request.method in SAFE_METHODS:
            return True
        elif request.method in OWNER_METHODS:
            return org.memberships.filter(
                user=request.user,
                role=constants.ORGANIZATION_ROLE_OWNER).exists()
        else:
            return False
