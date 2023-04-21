# Create your views here.
from post.models import Post
from post.serializers import PostSerializer
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


class PostViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.ListModelMixin,
                  mixins.DestroyModelMixin, GenericViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
