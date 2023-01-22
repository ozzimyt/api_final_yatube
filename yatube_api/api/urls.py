# TODO: JWT Token another del all
from django.urls import include, path
# from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import CommentViewSet, GroupViewSet, PostViewSet

router_v1 = DefaultRouter()

router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('posts/(?P<post_id>\\d+)/comments',
                   CommentViewSet, basename='comments')
router_v1.register('groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router_v1.urls)),
    # del it: path('v1/api-token-auth/', obtain_auth_token),
]
