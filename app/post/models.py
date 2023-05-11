import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class Category(models.Model):

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    category_title = models.CharField(max_length=200)


class Post(models.Model):

    def __str__(self):
        return self.post_title

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post_title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)

    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
