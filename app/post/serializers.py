from django.contrib.auth.models import User
from rest_framework import serializers

from post.models import Post, Category


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    category = serializers.StringRelatedField
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    def create(self, validated_data):
        return Post(**validated_data, user=self.context.get('request').user)

    class Meta:
        model = Post
        fields = '__all__'
