from django.urls import path
from mlmodels import views
from django.contrib.auth import views as t
urlpatterns=[

path('',views.home,name='home'),
path('login/',t.LoginView.as_view(template_name='mlmodels/login.html'),name="signin"),
path('signout/',t.LogoutView.as_view(template_name = 'mlmodels/signout.html'),name = 'signout'),

] 