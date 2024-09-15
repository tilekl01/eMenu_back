# Generated by Django 5.1.1 on 2024-09-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Salads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название')),
                ('image', models.ImageField(upload_to='products', verbose_name='Картинка')),
                ('description', models.TextField(default='No description available', verbose_name='Описание')),
                ('price', models.IntegerField(default=0, verbose_name='Цена')),
                ('currency', models.CharField(choices=[('C', 'Som'), ('$', 'Dollar')], default='$', max_length=100, verbose_name='Валюта')),
                ('is_active', models.BooleanField(default=True, verbose_name='Активный')),
            ],
            options={
                'verbose_name': 'Салат',
                'verbose_name_plural': 'Салаты',
            },
        ),
    ]
