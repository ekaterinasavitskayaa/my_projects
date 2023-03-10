# Generated by Django 4.1.3 on 2022-12-09 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0008_films_date_end_view_films_date_start_view'),
    ]

    operations = [
        migrations.AlterField(
            model_name='films',
            name='date_end_view',
            field=models.DateTimeField(default='2022-03-01 00:00', verbose_name='Конец показа'),
        ),
        migrations.AlterField(
            model_name='films',
            name='date_start_view',
            field=models.DateTimeField(default='2022-01-01 00:00', verbose_name='Начало показа'),
        ),
    ]
