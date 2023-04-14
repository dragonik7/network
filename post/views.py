# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from post.models import Post
from post.serializers import PostListSerializer


@api_view(['GET'])
def index(request):
	posts = Post.objects.order_by('-created_at')[:10]
	posts = PostListSerializer(posts, many=True)
	return Response(posts.data)


@api_view(['GET'])
def detail(request, post_id):
	post = Post.objects.get(uuid=post_id)
	post = PostListSerializer(post)
	return Response(post.data)


# @api_view(['POST'])
# def create(request):
