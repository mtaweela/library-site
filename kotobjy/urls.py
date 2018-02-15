from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'kotobjy'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.userHome, name='userHome'),
    path('profile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('age/', views.search_age, name='search_age'),
    path('search/', views.searchBook, name='searchBook'),
    url(r'^login/$', login, {'template_name': 'kotobjy/login.html'}),
    url(r'^logout/$', logout, {'next_page': 'kotobjy/index.html'}, name='logout'),
]