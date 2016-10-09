from rest_framework import serializers

from fragments.models import Post, Fragment


class PostSerializer(serializers.ModelSerialzer):
    """
    Serializer for Post instances
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'tldr',
            'author',
            'organization',
            'created',
            'updated',
        )
        read_only_field = (
            'created',
            'updated',
        )


class FragmentSerializer(serializers.ModelSerializer):
    """
    Serializer for Fragment instances
    """
    class Meta:
        model = Fragment
