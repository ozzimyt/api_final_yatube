from django.shortcuts import get_object_or_404
from rest_framework import filters, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import (
    IsAuthenticated,
    IsAuthenticatedOrReadOnly
)

from .mixins import FollowCreateListViewSet
from .permissions import IsAuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowingSerializer,
    GroupSerializer,
    PostSerializer
)

from posts.models import Group, Post


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # не понимаю почему, но если убрать IsAuthenticatedOrReadOnly ниже,
    # из пермишенов,то тесты валятся, несмотря на то, что он прописан дефолтным
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]
    pagination_class = LimitOffsetPagination
    throttle_scope = 'powerless_srv'

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    # не понимаю почему, но если убрать IsAuthenticatedOrReadOnly ниже,
    # из пермишенов,то тесты валятся, несмотря на то, что он прописан дефолтным
    permission_classes = [IsAuthorOrReadOnly, IsAuthenticatedOrReadOnly]

    def get_post(self):
        return get_object_or_404(Post, pk=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.select_related('author')

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class FollowingViewSet(FollowCreateListViewSet):
    serializer_class = FollowingSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',)

    def get_queryset(self):
        return self.request.user.follower.all()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
