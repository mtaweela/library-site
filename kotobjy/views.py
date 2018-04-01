from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView
from django.contrib.auth import login, logout, get_user_model, authenticate
from django.contrib.auth.decorators import login_required
from .forms import UserLoginForm, Search, UserRegisterForm
from django.core.paginator import Paginator


def index(request):
    searchform = Search()
    return render(request, 'kotobjy/index.html', {'searchform':searchform})


#################### users manipulation ######


@login_required(login_url='/kotobjy/login')
def userHome(request):
    searchform = Search()
    objects = Book.objects.all()
    
    p = Paginator(objects, 4)

    if request.POST.get("next"):
        if int(request.POST.get("next")) < p.num_pages:
            page = int( request.POST.get("next")) +1
        else:
            page = int( request.POST.get("next"))
    elif request.POST.get("previous"):
        if int(request.POST.get("previous")) > 1:
            page = int( request.POST.get("previous")) -1
        else:
            page = int( request.POST.get("previous"))
    else:
        page = 1

    if page <= p.num_pages and page > 0:
        bookList = p.page(page)
    else:
        bookList = []

    userpics = Ex_user.objects.all()


    # bookList = [bid.id for bid in latest_book_list]
    context = {
        'latest_book_list': bookList,
        'page': page,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/home.html', context)

@login_required(login_url='/kotobjy/login')
def Users(request):
    searchform = Search()
    objects = User.objects.all()
    p = Paginator(objects, 4)

    if request.POST.get("next"):
        if int(request.POST.get("next")) < p.num_pages:
            page = int( request.POST.get("next")) +1
        else:
            page = int( request.POST.get("next"))
    elif request.POST.get("previous"):
        if int(request.POST.get("previous")) > 1:
            page = int( request.POST.get("previous")) -1
        else:
            page = int( request.POST.get("previous"))
    else:
        page = 1

    if page <= p.num_pages and page > 0:
        usersList = p.page(page)
    else:
        usersList = []

    userpics = Ex_user.objects.all()

    i = 0
    userpicsmap = {}
    for user in usersList:
        if userpics.filter(user_id=user.id):
            userpicsmap[i] = userpics.filter(user_id=user.id)[0].pic
        else:
            userpicsmap[i] = "default.png"
        i+=1

    page = str(page)
    context = {
        'usersList': usersList,
        'userpicsmap': userpicsmap,
        'page': page,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/users.html', context)

# add user books and followed authors
@login_required(login_url='/kotobjy/login')
def user_profile(request, user_id):
    searchform = Search()
    user = User.objects.get(id=user_id)
    follows = Follow.objects.get(user_id_id=2)
    userpics = Ex_user.objects.all()
    if userpics.filter(user_id=user.id):
        userpic = userpics.filter(user_id=user.id)[0].pic
    else:
        userpic = "default.png"    
    context = {
        'user': user,
        'userpic': userpic,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/user.html', context)

#################### books manipulation ######

@login_required(login_url='/kotobjy/login')
def searchBook(request):
    searchform = Search()

    try:
        searchResult = Book.objects.filter(title=request.POST.get("search"))
        print(request.POST.get("search"))
    except Exception:
        results = []
        return render(request, 'kotobjy/search.html',{ 'searchform':searchform, 'results':results})
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
    
    rate = 3
    context = {
        'book': book,
        'searchform':searchform,
        'author': author,
        'rate': rate,
        'flag':flag
    }
    return render(request, 'kotobjy/bookDetail.html', context)

#################### author ######
@login_required(login_url='/kotobjy/login')
def authorDetail(request, author_id):
    searchform = Search()
    author = Author.objects.get(id=author_id)
    context = {
        'author': author,
        'searchform':searchform,
    }
    return render(request, 'kotobjy/authorDetail.html', context)

#################### logging and authentication ######


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