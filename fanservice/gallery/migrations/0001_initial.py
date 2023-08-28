# Generated by Django 4.2.4 on 2023-08-28 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='gallery/', verbose_name='Фото')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
            ],
            options={
                'verbose_name': 'Изображение',
                'verbose_name_plural': 'Изображения',
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Имя')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')),
                ('slug', models.SlugField(unique=True, verbose_name='url')),
                ('photos', models.ManyToManyField(to='gallery.photo', verbose_name='Фотографии')),
            ],
            options={
                'verbose_name': 'Галерея',
                'verbose_name_plural': 'Галереи',
            },
        ),
    ]
