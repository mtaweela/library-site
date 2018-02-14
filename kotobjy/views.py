from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)

def user_home(request):
    user_fav_books = User_fav.objects.all()
    latest_book_list = Book.objects.filter(category='user_fav_books[0]').order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)

def user_profile(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)

def search_age(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)