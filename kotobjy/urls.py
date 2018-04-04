from django.urls import path
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout
from django.contrib import admin

app_name = 'kotobjy'
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.userHome, name='userHome'),
    path('users/', views.Users, name='users'),
    path('userProfile/<int:user_id>/', views.user_profile, name='user_profile'),
    path('readlist/', views.Read, name='readlist'),
    path('wishlist/', views.Wish, name='wishlist'),   
    url(r'^register/$', views.register_view , name='register'),
    url(r'^login/$', views.login_view , name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    path('book/<int:book_id>/', views.bookDetail, name='bookDetail'),
    path('author/<int:authorId>/', views.authorDetail, name='authorDetail'),
    path('authorsList/', views.listAuthors, name='authorsList'),
    path('search/', views.searchBook, name='searchBook'),
]