from datetime import datetime

from django.db import models
from django.contrib.auth.models import AbstractUser


class CreateUpdateModelMixin(models.Model):
    create_time = models.DateTimeField(default=datetime.now, verbose_name='添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        abstract = True


class User(CreateUpdateModelMixin, models.Model):
    gender = (
        ('male', '男'),
        ('female', '女')
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=10, choices=gender,
                           default='male')

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['create_time']
        verbose_name = 'user'
        verbose_name_plural = verbose_name

