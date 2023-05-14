from django.contrib.auth.models import AbstractUser
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Specialty(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Специальность'
        verbose_name_plural = 'Специальности'


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


class Post(models.Model):
    TYPE_CHOICES = (
        ('news', 'Новость'),
        ('announcement', 'Объявление')
    )

    title = models.CharField(max_length=200)
    body = models.CharField(max_length=1000)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    views = models.ManyToManyField(User)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def is_news(self):
        return self.type == 'news'

    def is_announcement(self):
        return self.type == 'announcement'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'
