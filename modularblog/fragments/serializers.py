from django.utils.text import slugify

from rest_framework import serializers

from fragments.models import Post, Fragment


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


class PostSerializer(serializers.ModelSerializer):
    """
    Serializer for Post instances
    """
    fragments = FragmentSerializer(many=True, required=False)

    class Meta:
        model = Post
        fields = (
            'title',
            'slug',
            'tldr',
            'author',
            'fragments',
            'org',
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
        author = attrs.get('author')
        org = attrs.get('org')

        if author and org:
            if not org.is_member(author):
                raise serializers.ValidationError({
                    'organization': 'Author is not part of organization: %s' % (
                        org.name)
                })

        title = attrs.get('title')
        slug = attrs.get('slug')
        if title and not slug:
            attrs['slug'] = slugify(unicode(title))

        return attrs
