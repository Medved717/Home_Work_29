from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    email = models.EmailField(max_length=254, verbose_name='Адрес электронной почты.',
                              help_text='Введите адрес электронной почты.', unique=True)
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона', help_text='Введите номер телефона.',
                                    blank=True, null=True)
    avatar = models.ImageField(upload_to='users/avatars/', verbose_name='Аватар', help_text='Добавьте аватар.',
                               blank=True, null=True)
    country = models.CharField(max_length=100, verbose_name='Страна', help_text='Введите страну нахождения.',
                               blank=True, null=True)
    username = None

    token = models.CharField(max_length=100, verbose_name='token', blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email
