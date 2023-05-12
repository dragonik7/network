import uuid as uuid

from django.contrib.auth.models import AbstractUser
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class User(AbstractUser):
    COURSE_CHOICES = (
        (1, '1 курс'),
        (2, '2 курс'),
        (3, '3 курс'),
        (4, '4 курс'),
    )
    GROUP_CHOICES = (
        ('group1', 'Группа 1'),
        ('group2', 'Группа 2'),
        ('group3', 'Группа 3'),
    )
    PRIVILEGE_CHOICES = (
        ('regular', 'Обычный пользователь'),
        ('warden', 'Староста'),
        ('post_maker', 'Автор постов'),
    )

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE, verbose_name='Факультет')
    specialty = models.ForeignKey(Specialty, on_delete=models.CASCADE, verbose_name='Специальность')
    course = models.IntegerField(choices=COURSE_CHOICES, verbose_name='Курс')
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, verbose_name='Группа')
    privilege = models.CharField(max_length=20, choices=PRIVILEGE_CHOICES, verbose_name='Права')

    @property
    def is_regular(self):
        return self.privilege == 'regular'

    @property
    def is_warden(self):
        return self.privilege == 'warden'

    @property
    def is_post_maker(self):
        return self.privilege == 'post_maker'


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
