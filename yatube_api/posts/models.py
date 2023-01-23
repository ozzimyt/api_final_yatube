from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField('Название группы', max_length=200)
    slug = models.SlugField('Уникальный адрес', max_length=100, unique=True,)
    description = models.TextField('Описание группы', max_length=300)

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'

    def __str__(self):
        return self.title[:200]


class Post(models.Model):
    text = models.TextField(
        'Текст поста',
        help_text='Добавьте текст для новой записи'
    )
    pub_date = models.DateTimeField(
        'Дата публикации',
        auto_now_add=True
    )
    group = models.ForeignKey(
        Group,
        verbose_name='Группа',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='posts',
        help_text='Выберите группу для новой записи'
    )
    author = models.ForeignKey(
        User,
        verbose_name='Автор',
        on_delete=models.CASCADE,
        related_name='posts'
    )
    # TODO: Переделать
    # image = models.ImageField(
    #     'Изображение',
    #     upload_to='posts/',
    #     blank=True
    # )

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def __str__(self):
        return self.text[:499]


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        related_name='comments',
        verbose_name='Комментарий'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='comments',
        verbose_name='Автор комментария'
    )
    text = models.TextField(
        'Текст комментария',
        help_text='Напишите комментарий',
    )
    created = models.DateTimeField(
        'Дата добавления',
        auto_now_add=True,
    )

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'

    def __str__(self):
        return self.text[:99]


class Follow(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='follower',
        verbose_name='Подписчик'
    )
    following = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='following',
        verbose_name='Автор'
    )

    class Meta:
        verbose_name = 'подписчик'
        verbose_name_plural = 'подписчики'

    def __str__(self):
        return self.user.username
