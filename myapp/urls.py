from django.conf.urls import url, include
from myapp.views import list_view, detail_view, UserViewSet, GroupViewSet, PostViewSet, login_view, post_form_view
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users-api', UserViewSet)
router.register(r'groups-api', GroupViewSet)
router.register(r'posts-api', PostViewSet)

urlpatterns = [
    url(r'^posts/(?P<post_id>\d+)/$', detail_view, name="blog_detail"),
    url(r'^$', list_view, name="blog_index"),
    url(r'^postform', post_form_view, name="post_form"),
    url(r'^', include(router.urls)),
    url(r'^accounts/profile', login_view, name="login_success"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^accounts/', include('allauth.urls'))
]
