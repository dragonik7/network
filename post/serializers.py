from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Post


class PostListSerializer(serializers.ModelSerializer):
	user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

	class Meta:
		model = Post
		fields = ['uuid', 'title', 'text', 'category', 'created_at', 'user']
