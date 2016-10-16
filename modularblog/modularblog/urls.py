from django.conf.urls import url, include
from django.contrib import admin

from rest_framework_nested import routers

from fragments import views as fragment_views
from organizations import views as org_views


router = routers.SimpleRouter(trailing_slash=False)
router.register(r'orgs', org_views.OrgViewSet, base_name='orgs')

orgs_router = routers.NestedSimpleRouter(router, r'orgs', lookup='org',
                                         trailing_slash=False)
orgs_router.register(r'posts', fragment_views.PostViewSet, base_name='posts')

posts_router = routers.NestedSimpleRouter(orgs_router, r'posts', lookup='post',
                                          trailing_slash=False)
posts_router.register(r'fragments', fragment_views.FragmentViewset,
                      base_name='fragments')

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^', include(orgs_router.urls)),
    url(r'^', include(posts_router.urls)),
    url(r'^admin/', admin.site.urls),
]
