from rest_framework import mixins, viewsets


class FollowCreateListViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              viewsets.GenericViewSet):
    pass
