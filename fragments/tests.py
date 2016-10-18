from django.contrib.auth.models import User
from django.utils.text import slugify
from django.test import TransactionTestCase

from rest_framework.test import APIClient

from fragments import constants as fragments_constants
from fragments.models import Post, Fragment
from organizations.models import Organization


class PostAPITestCase(TransactionTestCase):
    """
    Test for posts
    """
    def setUp(self):
        self.org = Organization.objects.create(
            name='Fancy Trumpet Finally Located')

        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            username='johndoe')

        self.org.add_member(self.user)

    def test_create_post(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        post_data = {
            'title': 'There are no trumpets as fancy as this!',
            'tldr': 'Many trumpets have been invented so far. But there\'s '
                    'only one that stands out above all. It belongs to '
                    'Mrs. Peregrin'
        }

        response = client.post(
            '/orgs/%s/posts' % self.org.pk, post_data, format='json')

        self.assertEqual(response.status_code, 200, response.content)

        post = Post.objects.get()
        self.assertEqual(response.data['title'], post.title)

        fragment_data = {
            'post': post.pk,
            'order': 1,
            'fragment_type': fragments_constants.FRAGMENT_TYPE_PLAINTEXT,
            'content': 'For many years we\'ve sought to find the most perfect '\
                       'trumpet. We looked far & wide. One day we met Mrs. '\
                       'Peregring in the suburbs of Minneapolis. That\'s when '\
                       'we knew we found our trumpet.'
        }

        response = client.post(
            '/orgs/%s/posts/%s/fragments' % (self.org.pk, post.pk),
            fragment_data,
            format='json')

        self.assertEqual(response.status_code, 200, response.content)

        fragment = Fragment.objects.get()
        self.assertEqual(response.data['content'], fragment.content)

    def test_post_retrieval(self):
        post_title = u'Magical seal goes on a magical journey'

        post = Post.objects.create(
            title=post_title,
            slug=slugify(post_title),
            org=self.org,
            author=self.user)

        fragment = Fragment.objects.create(
            post=post,
            order=1,
            fragment_type=fragments_constants.FRAGMENT_TYPE_PLAINTEXT,
            content='Once upon a time there was a magical seal. He went on a '\
                    'magical journey')

        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.get('/orgs/%s/posts' % self.org.pk)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

        post_data = response.data[0]

        self.assertEqual(post_data['title'], post.title)
        self.assertEqual(len(post_data['fragments']), 1)

        fragment_data = post_data['fragments'][0]
        self.assertEqual(fragment_data['content'], fragment.content)
