# Generated by Django 4.2.6 on 2023-10-27 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='Категории')),
            ],
            options={
                'verbose_name': 'Категории',
                'verbose_name_plural': 'Категории',
            },
        ),
        migrations.CreateModel(
            name='Items',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(max_length=20, verbose_name='Имя объекта')),
                ('slug', models.SlugField(unique=True, verbose_name='URL')),
                ('cat', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='Menu.categories', verbose_name='Категория')),
            ],
            options={
                'verbose_name': 'Подпункты',
                'verbose_name_plural': 'Подпункты',
            },
        ),
    ]
