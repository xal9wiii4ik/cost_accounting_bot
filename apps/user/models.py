from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """Переопределение модели пользователь"""

    chat_id = models.BigIntegerField(verbose_name='Айди чата пользователя', default=0, null=True)

    def __str__(self):
        return f'id: {self.pk}, chat_id: {self.chat_id}, username: {self.username}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class UserQueue(models.Model):
    """Очередь пользователей для добавления"""

    chat_id = models.BigIntegerField(verbose_name='Айди чата пользователя', default=0, null=True)
    username = models.CharField(max_length=150, unique=True)
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return f'chat_id: {self.chat_id}, username: {self.username}, ' \
               f'first_name: {self.first_name}, last_name: {self.last_name}'

    class Meta:
        verbose_name = 'Пользователь в очередь'
        verbose_name_plural = 'Очередь пользователей'
