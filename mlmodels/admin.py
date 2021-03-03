from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Programming)
admin.site.register(Course)