from django.contrib import admin

from modularblog.core.admin import BaseAdmin

from fragments.models import Post, Fragment


@admin.register(Post)
class PostAdmin(BaseAdmin):
    list_display = ('pk', 'title', 'author', 'org', 'state', 'created',)
    search_fields = [
        'title',
        'author__username',
    ]
    display_as_charfield = ['title', 'slug']
    display_as_choicefield = ['state']


@admin.register(Fragment)
class FragmentAdmin(BaseAdmin):
    list_display = ('pk', 'post', 'fragment_type', 'order', 'created',)
    search_fields = [
        'post__title',
        'content',
    ]
    display_as_charfield = ['title', 'slug']
    display_as_choicefield = ['fragment_type']
