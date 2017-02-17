from django.contrib import admin

from modularblog.core.admin import BaseAdmin
from organizations.models import Organization, Membership


@admin.register(Organization)
class OrganizationAdmin(BaseAdmin):
    list_display = ('pk', 'name', 'slug', 'owner', 'created',)
    search_fields = [
        'name',
    ]
    display_as_charfield = ['name', 'slug']

    def owner(self, obj):
        return obj.owner and obj.owner.username or ''


@admin.register(Membership)
class MembershipAdmin(BaseAdmin):
    list_display = ('pk', 'user', 'org', 'role', 'created',)
    search_fields = [
        'org__name',
        'user__username'
    ]
    display_as_choicefield = ['role']
