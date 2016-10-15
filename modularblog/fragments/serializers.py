from rest_framework import serializers

from fragments.models import Post, Fragment


class PostSerializer(serializers.ModelSerializer):
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
        fields = (
            'post',
            'fragment_type',
            'order',
            'content',
            'is_sanitized',
            'credit',
            'caption',
            'language',
            'embed_type',
            'created',
            'updated',
        )
        read_only_field = (
            'created',
            'updated',
        )
