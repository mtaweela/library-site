from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Book, Author, Author_books


def index(request):
    pass


def auth(request):
    pass


def bookDetail(request, book_id):
    book = Book.objects.get(id=book_id)
    # author = Author.objects.get(Author_books.objects.get(book_id=book_id).author_id)
    context = {'book': book}
    return render(request, 'Kotobjy/book_detail.html', context)

# def authorDetail(request, auth_id):
#     author = Authoe.objects.get(id=auth_id)
#     # author = Author.objects.get(Author_books.objects.get(book_id=book_id).author_id)
#     context = {'book': book}
#     return render(request, 'Kotobjy/book_detail.html', context)
