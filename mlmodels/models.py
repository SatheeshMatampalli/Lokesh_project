from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save


class Programming(models.Model):
	name=models.CharField(max_length=90)

	def __str__(self):
		return self.name

class Course(models.Model):
	programming=models.ForeignKey(Programming,on_delete=models.CASCADE)
	name=models.CharField(max_length=100)
	def __str__(self):
		return self.name