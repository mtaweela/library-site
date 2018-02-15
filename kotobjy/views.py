from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import Permission, User
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import Book, Author, Author_books
from django.views.generic.list import ListView


class BookListView(ListView):
    model = Book


def bookDetail(request, book_id):
    book = Book.objects.get(id=book_id)
    aid = Author_books.objects.get(book_id=book.id).author_id_id
    author = Author.objects.get(id=aid)
    context = {'book': book, 'author': author}
    return render(request, 'Kotobjy/book_detail.html', context)


def authorDetail(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {'author': author}
    return render(request, 'Kotobjy/author_detail.html', context)
