from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView

from .forms import Search

def index(request):
    searchform = Search()
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/index.html', context)

def userHome(request):
    searchform = Search()
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    bookList = [bid.id for bid in latest_book_list]
    context = {
        'latest_book_list': latest_book_list,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/index.html', context)

def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    follows = Follow.objects.get(user_id_id=2)
    context = {
        'user': user,
    }
    return render(request, 'kotobjy/user.html', context)


def searchBook(request):
    searchform = Search()

    try:
        searchResult = Book.objects.filter(title=request.POST.get("search"))
        print(request.POST.get("search"))
    except Exception:
        results = []
        return render(request, 'kotobjy/search.html',{ 'results':results})
    else:
        results = searchResult
        return render(request, 'kotobjy/search.html',{ 'searchform':searchform, 'results':results})




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

