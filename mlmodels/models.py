from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

class Techniques(models.Model):
	modeltype=[('Classification','Classification'),('Regression','Regression')]
	modelsml=models.CharField(max_length=20,choices=modeltype)
	is_status=models.IntegerField(default=0,max_length=4)