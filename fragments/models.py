"""
Models defining the Modular Blog
"""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from fragments import constants


class Organization(models.Model):
    """
    Organization structure to allow multiple users to group
    """
    name = models.TextField()
    slug = models.TextField()
    description = models.TextField()
    owner = models.ForeignKey(User, related_name='organizations')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    """
    The primary entity that connects different components
    """
    title = models.TextField()
    author = models.ForeignKey(User, related_name='posts')
    tldr = models.TextField()
    slug = models.TextField()
    organization = models.ForeignKey(Organization, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class BaseFragment(models.Model):
    """
    A section of the post that only contains plain text
    """
    post = models.ForeignKey(Post, related_name='fragments')
    fragment_type = models.TextField(choices=constants.FRAGMENT_TYPE_CHOICES)
    order = models.IntegerField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '{} fragment of post: {}'.format(
            self.get_fragment_type_display(),
            self.post)
