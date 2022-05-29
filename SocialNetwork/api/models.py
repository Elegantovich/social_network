from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):

    email = models.EmailField(
        db_index=True,
        unique=True,
        max_length=254,
        verbose_name='Электронная почта'
        )
    first_name = models.CharField(
        max_length=150,
        verbose_name='Имя'
        )
    last_name = models.CharField(
        max_length=150,
        verbose_name='Фамилия'
        )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'password']

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.username


class Post(models.Model):

    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts',
        verbose_name='Автор'
        )
    name = models.CharField(
        max_length=200,
        verbose_name='Название поста'
        )
    text = models.TextField(
        verbose_name='Описание поста'
        )
    pub_date = models.DateField(
        auto_now_add=True,
        verbose_name='Дата создания',
        )
    is_favorite = models.BooleanField(
        default=False,
        verbose_name='Добавить в избранное',
    )

    class Meta:

        ordering = ('-pub_date', )

    def __str__(self):
        return self.name


class Favorite(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
        )
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        related_name='favorites',
        verbose_name='Пост',
        )

    class Meta:
        ordering = ['-id']

    def __str__(self):

        return f'{self.post} {self.user}'
