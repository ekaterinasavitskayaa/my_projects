from django.db import models
from django.urls import reverse


class Films(models.Model):
    title = models.CharField(max_length=150, verbose_name='Наименование')
    content = models.TextField(verbose_name='Контент')
    directed_by = models.CharField(max_length=150, verbose_name='Режиссер')
    starring = models.CharField(max_length=150, verbose_name='В главной роли', blank=True)
    release_date = models.CharField(max_length=150, verbose_name='Дата выхода', blank=True)
    running_time = models.CharField(max_length=150, verbose_name='Продолжительность')
    age = models.IntegerField(verbose_name='Возраст')
    photo = models.ImageField(upload_to='photos/%Y/%m/%d', blank=True, verbose_name='Фото')
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')
    date_start_view = models.DateField(verbose_name='Начало показа', default='2022-01-01')
    date_end_view = models.DateField(verbose_name='Конец показа', default='2022-03-01')
    category = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name='Категория')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('view_films', kwargs={'films_id': self.pk})

    class Meta:
        verbose_name = 'Фильм'
        verbose_name_plural = 'Фильмы'
        ordering = ['id']


class Category(models.Model):
    title = models.CharField(max_length=150, db_index=True, verbose_name='Наименование категории')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['title']

