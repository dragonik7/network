import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

    def __str__(self):
        return self.title

    CATEGORY = [
        (1, 'Post'),
        (2, 'Notice'),
    ]

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=200)
    text = models.CharField(max_length=1000)

    category = models.IntegerField(choices=CATEGORY, default=1)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
