from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, Search, UserRegisterForm

# this is the page before logging in 
def index(request):
    searchform = Search()
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/index.html', context)

# this the main page user is directed to once he log in
@login_required(login_url='/kotobjy/login')
def userHome(request):
    searchform = Search()
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    bookList = [bid.id for bid in latest_book_list]
    context = {
        'latest_book_list': latest_book_list,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/index.html', context)

@login_required(login_url='/kotobjy/login')
def user_profile(request, user_id):
    searchform = Search()
    user = User.objects.get(id=user_id)
    follows = Follow.objects.get(user_id_id=2)
    context = {
        'user': user,
        'searchform':searchform,
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

@login_required(login_url='/kotobjy/login')
def bookDetail(request, book_id):
    searchform = Search()
    book = Book.objects.get(id=book_id)
    aid = Author_books.objects.filter(book_id=book.id)
    
    if not aid:
        flag = False
        author = 0
    else:
        flag = True
        authId = aid[0].author_id_id
        author = Author.objects.get(id=authId)
    
    context = {
        'book': book,
        'searchform':searchform,
        'author': author,
        'flag':flag
    }
    return render(request, 'kotobjy/bookDetail.html', context)

@login_required(login_url='/kotobjy/login')
def authorDetail(request, author_id):
    searchform = Search()
    author = Author.objects.get(id=author_id)
    context = {'author': author}
    return render(request, 'kotobjy/authorDetail.html', context)

# logging and authentication 

def login_view(request):
    searchform = Search()
    next = request.GET.get('next')
    form = UserLoginForm(request.POST or None)
    title = "Login"
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect("/kotobjy/home")

    return render(request, "kotobjy/form.html", {'searchform':searchform, "form":form, "title": title})

def register_view(request):
    searchform = Search()
    next = request.GET.get('next')
    title = "Register"
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()

        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect("/kotobjy/home")
    return render(request, "kotobjy/form.html", {'searchform':searchform, "form":form, "title": title})

def logout_view(request):
    logout(request)
    return redirect("/kotobjy/")