from django.contrib.auth.models import User
from django.db import models


class Facult(models.Model):
    title = models.CharField(max_length=100)


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    course = models.IntegerField()
    group = models.IntegerField()
    facult = models.ForeignKey(Facult, on_delete=models.PROTECT)
