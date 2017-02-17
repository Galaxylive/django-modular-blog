from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

from organizations import constants


class Organization(models.Model):
    """
    Organization structure to allow multiple users to group
    """
    name = models.TextField(unique=True)
    slug = models.TextField()
    description = models.TextField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.name

    @property
    def owner(self):
        owner_membership = self.memberships.filter(
            role=constants.ORGANIZATION_ROLE_OWNER).first()

        return owner_membership is not None and owner_membership.user or None

    def add_member(self, user, role=None):
        membership_data = {
            'org': self,
            'user': user
        }

        if role is not None:
            membership_data.update({
                'role': role
            })

        self.memberships.create(**membership_data)

    def is_member(self, user):
        return self.memberships.filter(user=user).exists()


class Membership(models.Model):
    """
    Describe membership for organization
    """
    org = models.ForeignKey(Organization, related_name='memberships')
    user = models.ForeignKey(User, related_name='memberships')
    role = models.TextField(
        choices=constants.ORGANIZATION_ROLE_CHOICES,
        default=constants.ORGANIZATION_ROLE_MEMBER)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return '%s, %s of Org: %s' % (self.user.username, self.role, self.org)

    class Meta:
        unique_together = ('org', 'user',)
