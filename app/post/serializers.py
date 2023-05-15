from rest_framework import serializers

from post.models import Post, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'faculty', 'password', 'specialty', 'course', 'group', 'email')


class PostSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        read_only=True,
        slug_field='id',
    )

    def create(self, validated_data):
        return Post(**validated_data, user=self.context.get('request').user)

    class Meta:
        model = Post
        fields = '__all__'
