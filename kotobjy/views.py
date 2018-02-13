from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Books, Author

def index(request):
    pass

def auth(request):
    pass