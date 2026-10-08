from django.db import models


class Blog(models.Model):
    heading = models.CharField(max_length=100, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Содержимое')
    preview = models.ImageField(verbose_name='Изображение', upload_to='blog/', blank=True, null=True)
    create_at = models.DateTimeField(verbose_name='Дата создания', auto_now_add=True)
    quantity_views = models.PositiveIntegerField(verbose_name='Количество просмотров',
                                                 help_text='Ведется подсчет количество просмотров объекта',
                                                 default=0)
    is_published = models.BooleanField(verbose_name='Опубликовано', help_text='Отметьте факт опубликования статьи.',
                                       default=False)

    class Meta:
        verbose_name = 'Блог'
        verbose_name_plural = 'Блоги'
        ordering = ['create_at', 'heading']
