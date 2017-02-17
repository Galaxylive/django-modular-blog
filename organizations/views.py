from rest_framework import viewsets

from organizations.models import Organization
from organizations.permissions import OrgPermissions
from organizations.serializers import OrgSerializer


class OrgViewSet(viewsets.ModelViewSet):
    """
    API endpoints for Organizations
    """

    http_method_names = ['options', 'head', 'get', 'patch']
    queryset = Organization.objects.all()
    permission_classes = (OrgPermissions,)
    serializer_class = OrgSerializer
