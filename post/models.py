import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Посты'

	class Category(models.IntegerChoices):
		POST = 1
		NOTICE = 2

	uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	title = models.CharField(max_length=200)
	text = models.TextField()

	category = models.IntegerField(choices=Category.choices, default=Category.POST)
	user = models.ForeignKey(User, on_delete=models.PROTECT)
	created_at = models.DateTimeField(auto_now_add=True)
