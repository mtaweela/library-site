from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib import admin

app_name = 'kotobjy'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.userHome, name='userHome'),
    path('userProfile/<int:user_id>/', views.user_profile, name='user_profile'),
    url(r'^register/$', views.register_view , name='register'),
    url(r'^login/$', views.login_view , name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    path('book/<int:book_id>/', views.bookDetail, name='bookDetail'),
    path('author/<int:author_id>/', views.authorDetail, name='authorDetail'),
    path('search/', views.searchBook, name='searchBook'),
]