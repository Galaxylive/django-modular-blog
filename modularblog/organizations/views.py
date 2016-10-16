from rest_framework import viewsets

from organizations.permissions import OrgPermissions
from organizations.serializers import OrgSerializer


class OrgViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Organizations
    """
    permission_classes = (OrgPermissions,)
    serializer_class = OrgSerializer
    http_method_names = ['options', 'head', 'get', 'patch']
