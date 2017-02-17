from django.utils.text import slugify

from rest_framework import serializers

from organizations.models import Organization


class OrgSerializer(serializers.ModelSerializer):
    """
    Serializer for Organization instances
    """
    class Meta:
        model = Organization
        fields = (
            'name',
            'slug',
            'description',
            'created',
            'updated',
        )
        read_only_field = (
            'created',
            'updated',
        )
        extra_kwargs = {
            'slug': {'required': False}
        }

    def validate(self, attrs):
        name = attrs.get('name')
        slug = attrs.get('slug')

        if name and not slug:
            attrs['slug'] = slugify(unicode(name))

        return attrs
