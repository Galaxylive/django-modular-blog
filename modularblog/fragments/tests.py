from django.contrib.auth.models import User
from django.test import TransactionTestCase

from rest_framework.test import APIClient

from organizations.models import Organization


class PostAPITestCase(TransactionTestCase):
    """
    Test for posts
    """
    def setUp(self):
        self.org = Organization.objects.create(
            name='Fancy Trumpets')

        self.user = User.objects.create(
            first_name='John',
            last_name='Doe',
            email='johndoe@example.com',
            username='johndoe')

        self.org.add_member(self.user)

    def test_create_post(self):
        post_data = {
            'title': 'There are no trumpets as fancy as this!',
            'tldr': 'Many trumpets have been invented so far. But there\'s '
                    'only one that stands out above all. It belongs to '
                    'Mrs. Peregrin'
        }

        client = APIClient()
        client.force_authenticate(user=self.user)
        response = client.post(
            '/orgs/%s/posts' % self.org.pk, post_data, format='json')

        self.assertEqual(response.status_code, 200, response.content)
