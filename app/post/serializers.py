import uuid

from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from post.models import Post, User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
    )

    class Meta:
        model = User
        fields = ('first_name', 'faculty', 'password', 'specialty', 'course', 'group', 'email')

    def create(self, validated_data):
        return User.objects.create(
            username=uuid.uuid4(),
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            course=validated_data['course'],
            group=validated_data['group'],
            faculty=validated_data['faculty'],
            specialty=validated_data['specialty'],
            password=make_password(validated_data['password'])
        )


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
