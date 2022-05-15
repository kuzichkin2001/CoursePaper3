# Generated by Django 4.0.4 on 2022-05-15 14:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Session',
            fields=[
                ('session_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(default='', max_length=200, verbose_name='Новый проект <django.db.models.fields.AutoField>')),
                ('kuz_place', models.IntegerField(default=0)),
                ('code', models.TextField(default='')),
                ('creation_date', models.DateTimeField(default=datetime.datetime(2022, 5, 15, 9, 33, 55, 520079))),
            ],
        ),
        migrations.CreateModel(
            name='WorkSpace',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fixed_jumps', models.CharField(max_length=200, verbose_name='Фиксированный шаг')),
                ('random_jumps', models.CharField(max_length=200, verbose_name='Произвольные шаги')),
                ('code_input', models.TextField(verbose_name='Напишите код программы')),
            ],
        ),
    ]
