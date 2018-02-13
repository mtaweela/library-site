from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login

app_name = 'kotobjy'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/kotobjy/', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'kotobjy/login.html'}),
]