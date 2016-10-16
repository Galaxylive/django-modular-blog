from django.db.models import Q

from rest_framework import viewsets
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from fragments import constants
from fragments.permissions import IsOrgMember
from fragments.models import Post, Fragment
from fragments.serializers import PostSerializer, FragmentSerializer
from organizations.models import Organization


class BaseViewSet(viewsets.ViewSet):
    """
    Base viewset for Post & Fragment API endpoints
    """
    permission_classes = (IsOrgMember,)

    def _get_object_or_404(self, model, params):
        try:
            obj = model.objects.get(**params)
        except model.DoesNotExist:
            raise NotFound

        return obj


class PostViewSet(BaseViewSet):
    """
    API endpoints for posts
    """

    def list(self, request, org_pk, pk=None):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        posts = org.posts.all()

        if not org.is_member(request.user):
            posts = posts.filter(state=constants.POST_STATE_PUBLISHED)

        serializer = PostSerializer(posts, many=True)
        return Response(serializer.data)

    def retrieve(self, request, org_pk, pk):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        params = {'org': org, 'pk': pk}
        if not org.is_member(request.user):
            params.update({
                'state': constants.POST_STATE_PUBLISHED
            })

        post = self._get_object_or_404(Post, params)

        serializer = PostSerializer(post)
        return Response(serializer.data)

    def create(self, request, org_pk, pk=None):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        self.check_object_permissions(self.request, org)

        post_data = request.data.copy()
        post_data.update({
            'author': request.user.pk,
            'org': org
        })

        serializer = PostSerializer(data=post_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status_code=400)

        serializer.save()
        return Response(serializer.data, status_code=200)

    def partial_update(self, request, org_pk, pk):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        self.check_object_permissions(self.request, org)

        post = self._get_object_or_404(Post, {'org': org, 'pk': pk,})

        serializer = PostSerializer(post, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status_code=400)

        serializer.save()
        return Response(serializer.data, status_code=200)


class FragmentViewset(BaseViewSet):
    """
    API endpoints for fragments
    """

    def list(self, request, org_pk, post_pk, pk=None):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        post_params = {'org': org, 'pk': post_pk}
        if not org.is_member(request.user):
            post_params.update({
                'state': constants.POST_STATE_PUBLISHED
            })
        post = self._get_object_or_404(Post, post_params)

        serializer = FragmentSerializer(post.fragments.all(), many=True)
        return Response(serializer.data)

    def retrieve(self, request, org_pk, post_pk, pk):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        post_params = {'org': org, 'pk': post_pk}
        if not org.is_member(request.user):
            post_params.update({
                'state': constants.POST_STATE_PUBLISHED
            })
        post = self._get_object_or_404(Post, post_params)
        fragment = self._get_object_or_404(Fragment, {'post': post, 'pk': pk})

        serializer = FragmentSerializer(fragment)
        return Response(serializer.data)

    def create(self, request, org_pk, post_pk, pk=None):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        self.check_object_permissions(self.request, org)

        post = self._get_object_or_404(Post, {'org': org, 'pk': post_pk})

        fragment_data = request.data.copy()
        fragment_data.update({
            'post': post.pk,
            'org': org
        })

        serializer = FragmentSerializer(data=fragment_data)
        if not serializer.is_valid():
            return Response(serializer.errors, status_code=400)

        serializer.save()
        return Response(serializer.data, status_code=200)

    def partial_update(self, request, org_pk, post_pk, pk):
        org = self._get_object_or_404(Organization, {'pk': org_pk})

        self.check_object_permissions(self.request, org)

        post = self._get_object_or_404(Post, {'org': org, 'pk': post_pk})

        fragment = self._get_object_or_404(Fragment, {'post': post, 'pk': pk})

        serializer = PostSerializer(fragment, data=request.data, partial=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status_code=400)

        serializer.save()
        return Response(serializer.data, status_code=200)
