# Generated by Django 4.0.4 on 2022-05-15 15:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hopper', '0002_alter_session_creation_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=80)),
                ('role', models.CharField(max_length=80)),
            ],
        ),
        migrations.AlterField(
            model_name='session',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 5, 15, 10, 6, 16, 830445)),
        ),
        migrations.AddField(
            model_name='session',
            name='user_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='hopper.user'),
        ),
    ]
