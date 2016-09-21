from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models


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
