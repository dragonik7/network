# Create your views here.
from django_filters.rest_framework import DjangoFilterBackend
from drf_spectacular.utils import extend_schema
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet

from post.models import Post, User
from post.permissions import CanCreatePosts, CanCreateNews
from post.serializers import PostSerializer, UserSerializer


@extend_schema(
    tags=['Post'],
    auth=[{"Bearer": []}]
)
class PostViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.ListModelMixin,
                  GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['type']
    permission_classes = [CanCreatePosts, CanCreateNews]


@extend_schema(
    tags=['User']
)
class UserViewSet(mixins.CreateModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
