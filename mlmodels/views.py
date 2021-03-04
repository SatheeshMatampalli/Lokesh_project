from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.contrib.auth.models import User
from .models import *
# Create your views here.
def home(req):
	return render(req,'mlmodels/home.html')

def index(req):
	if req.method=="POST":
		print(req.POST['programming'])
		print(req.POST['courses'])
	data=MLtypes.objects.all()
	return render(req,'mlmodels/index.html',{'data':data})

def load_courses(req):
	programming_id=req.GET.get('programming')
	print(programming_id)
	courses=MLmodels.objects.filter(programming_id=programming_id).order_by('name')
	print(courses)
	return render(req,'mlmodels/dropd.html',{'courses':courses})


