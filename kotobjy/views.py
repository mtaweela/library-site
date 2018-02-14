from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
<<<<<<< HEAD
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
=======
from .models import Book

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)
>>>>>>> 3a6fe4e0feb87a3d32cf5bdf032e1044b0dbb6ef
