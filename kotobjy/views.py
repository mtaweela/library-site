from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import loader
from django.urls import reverse
from .models import *
from django.views.generic import ListView, DetailView

from .forms import Search

def index(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)

def userHome(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    bookList = [bid.id for bid in latest_book_list]
    authorBooks = Author_books.objects.all()
    authorId = [authorBooks.filter(book_id_id=id)[0].author_id.id for id in bookList ]
    author = [Author.objects.filter(id=Id)[0].name for Id in authorId ]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)

def user_profile(request, user_id): 
    user = User.objects.get(id=user_id)
    follows = Follow.objects.get(user_id_id=2)
    context = {
        'user': user,
    }
    return render(request, 'kotobjy/user.html', context)

def search_age(request):
    latest_book_list = Book.objects.order_by('-pub_date')[:5]
    context = {
        'latest_book_list': latest_book_list,
    }
    return render(request, 'kotobjy/index.html', context)


def searchBook(request):
    form = Search()
    
    # try:
    searchResult = Book.objects.get(title='new')
    print(request.POST.get("search"))
    
    # except (KeyError, search.DoesNotExist):
    #     return HttpResponse("no")
    # else:
    return render(request, 'kotobjy/search.html',{'form':form})


    # try:
    #     selected_choice = question.choice_set.get(pk=request.POST['choice'])
    # except (KeyError, Choice.DoesNotExist):
    #     # Redisplay the question voting form.
    #     return render(request, 'polls/detail.html', {
    #         'question': question,
    #         'error_message': "You didn't select a choice.",
    #     })
    # else:
    #     selected_choice.votes += 1
    #     selected_choice.save()
    #     # Always return an HttpResponseRedirect after successfully dealing
    #     # with POST data. This prevents data from being posted twice if a
    #     # user hits the Back button.
    #     return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

    # def search(request):
    # form = AddBookForm()
    # try:
    #     searchResult = Book.objects.get(title=request.POST.get("search","new"))
    # except (KeyError, search.DoesNotExist):
    #         return render(request, 'kotobjy/index.html',{'form': form})
