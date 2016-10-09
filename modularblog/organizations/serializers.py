from rest_framework import serializers

from organizations.models import Organization


class OrganizationSerializer(serializers.ModelSerialzer):
    """
    Serializer for Organization instances
    """
    class Meta:
        model = Organization
        fields = (
            'name',
            'slug',
            'description',
            'owner',
            'created',
            'updated',
        )
        read_only_field = (
            'name',
            'owner',
            'created',
            'updated',
        )
