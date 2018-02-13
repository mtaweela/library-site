from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    template = loader.get_template('kotobjy/index.html')
    context = {
        'latest_book_list': latest_book_list,
    }
    return HttpResponse(template.render(context, request))