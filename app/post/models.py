import uuid as uuid

from django.contrib.auth.models import User
from django.db import models


from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    FACULTY_CHOICES = (
        ('faculty1', 'Факультет 1'),
        ('faculty2', 'Факультет 2'),
        ('faculty3', 'Факультет 3'),
    )
    SPECIALTY_CHOICES = (
        ('specialty1', 'Специальность 1'),
        ('specialty2', 'Специальность 2'),
        ('specialty3', 'Специальность 3'),
    )
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
    REGULAR = 'regular'
    WARDEN = 'warden'
    POST_MAKER = 'post_maker'
    PRIVILEGE_CHOICES = (
        (REGULAR, 'Обычный пользователь'),
        (WARDEN, 'Староста'),
        (POST_MAKER, 'Автор постов'),
    )

    first_name = models.CharField(max_length=30, verbose_name='Имя')
    faculty = models.CharField(max_length=20, choices=FACULTY_CHOICES, verbose_name='Факультет')
    specialty = models.CharField(max_length=20, choices=SPECIALTY_CHOICES, verbose_name='Специальность')
    course = models.IntegerField(choices=COURSE_CHOICES, verbose_name='Курс')
    group = models.CharField(max_length=20, choices=GROUP_CHOICES, verbose_name='Группа')
    privilege = models.CharField(max_length=20, choices=PRIVILEGE_CHOICES, default=REGULAR, verbose_name='Права')

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
