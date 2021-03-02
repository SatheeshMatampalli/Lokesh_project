from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
# Create your views here.
def home(req):
	return render(req,'mlmodels/home.html')