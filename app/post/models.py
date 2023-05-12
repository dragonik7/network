import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


class Faculty(models.Model):
    title = models.CharField(max_length=100)


class Specialty(models.Model):
    title = models.CharField(max_length=100)


class Student(models.Model):
    permission_user = (
        (0, 'regular'),
        (1, 'warden'),
        (2, 'post_maker'),
    )
    name = models.CharField(max_length=255)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    faculty = models.ForeignKey(Faculty, on_delete=models.PROTECT)
    specialty = models.ForeignKey(Specialty, on_delete=models.PROTECT)
    course = models.IntegerField()
    group = models.IntegerField()
    permission = models.IntegerField(choices=permission_user)


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
    user = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
