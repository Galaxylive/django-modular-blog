"""
Models defining the composing section of Modular blog
"""
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres import fields as pgfields

from fragments import constants
from organizations.models import Organization



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
    Base definition of different components of the post
    """
    order = models.IntegerField()
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __unicode__(self):
        return '{} fragment of post: {}'.format(
            self.get_fragment_type_display(),
            self.post)


class PlainTextFragment(models.Model):
    """
    A section of the post that only contains plain text
    """
    post = models.ForeignKey(Post, related_name='plain_text_fragments')


class HTMLFragment(models.Model):
    """
    A section of the post that contains HTML
    """
    post = models.ForeignKey(Post, related_name='html_fragments')
    is_sanitized = models.BooleanField(default=False)


class MarkdownFragment(models.Model):
    """
    A section of the post that contains HTML
    """
    post = models.ForeignKey(Post, related_name='markdown_fragments')


class ImageFragment(models.Model):
    """
    A section of the post that contains HTML
    """
    post = models.ForeignKey(Post, related_name='image_fragments')
    caption = models.TextField(blank=True)


class CodeFragment(models.Model):
    """
    A section of the post that contains HTML
    """
    post = models.ForeignKey(Post, related_name='code_fragments')
    language = models.TextField(
        choices=constants.CODE_LANGUAGE_CHOICES,
        default=constants.CODE_LANGUAGE_GENERIC)


class EmbedFragment(models.Model):
    """
    A section of the post that contains HTML
    """
    post = models.ForeignKey(Post, related_name='embed_fragments')
    embed_type = models.TextField(
        choices=constants.EMBED_TYPE_CHOICES,
        default=constants.EMBED_TYPE_RAW)
