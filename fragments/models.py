"""
Models defining the composing section of Modular blog
"""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify

from fragments import constants
from organizations.models import Organization


class Post(models.Model):
    """
    The primary entity that connects different components
    """
    title = models.TextField()
    slug = models.TextField()
    author = models.ForeignKey(User, related_name='posts')
    tldr = models.TextField(blank=True)
    org = models.ForeignKey(Organization, related_name='posts')
    state = models.TextField(
        choices=constants.POST_STATE_CHOICES,
        default=constants.POST_STATE_DRAFT)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-updated',)

    def __unicode__(self):
        return self.title


class Fragment(models.Model):
    """
    Base definition of different components of the post
    """
    post = models.ForeignKey(Post, related_name='fragments')
    order = models.IntegerField()
    content = models.TextField()
    fragment_type = models.TextField(
        choices=constants.FRAGMENT_TYPE_CHOICES,
        default=constants.FRAGMENT_TYPE_PLAINTEXT)
    is_sanitized = models.BooleanField(default=False)
    credit = models.TextField(blank=True)
    caption = models.TextField(blank=True)
    # Used by code fragments
    language = models.TextField(
        choices=constants.CODE_LANGUAGE_CHOICES, blank=True)
    # Used by embed fragments
    embed_type = models.TextField(
        choices=constants.EMBED_TYPE_CHOICES, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('order',)

    def __unicode__(self):
        return '{} fragment of post: {}'.format(
            self.fragment_type,
            self.post)
