import datetime
from django.db import models


# Create your models here.
class WorkSpace(models.Model):
	fixed_jumps = models.CharField('Фиксированный шаг', max_length=200)
	random_jumps = models.CharField('Произвольные шаги', max_length=200)
	code_input = models.TextField('Напишите код программы')


class User(models.Model):
	user_id = models.AutoField(primary_key=True)
	username = models.CharField(null=False, max_length=30)
	password = models.CharField(null=False, max_length=80)
	role = models.CharField(null=False, max_length=80)


class Session(models.Model):
	session_id = models.AutoField(unique=True, primary_key=True)
	name = models.CharField('Новый проект %s' % session_id, max_length=200, null=False, default='')
	kuz_place = models.IntegerField(default=0, null=False)
	code = models.TextField(default='')
	creation_date = models.DateTimeField(default=datetime.datetime.now())
	user_id = models.ForeignKey(User, on_delete=models.CASCADE, to_field='user_id', default=1)
