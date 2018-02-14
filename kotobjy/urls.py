from django.urls import path
<<<<<<< HEAD
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:book_id>/', views.bookDetail, name='book_detail'),
    # path('<int:author_id>/', views.authorDetail, name='author_detail'),
]
=======
from django.conf.urls import url
from . import views
from django.contrib.auth.views import login, logout

app_name = 'kotobjy'
urlpatterns = [
    path('', views.index, name='index'),
    path('login/kotobjy/', views.index, name='index'),
    url(r'^login/$', login, {'template_name': 'kotobjy/login.html'}),
    url(r'^logout/$', logout, {'next_page': 'kotobjy/index.html'}, name='logout'),
]
>>>>>>> 3a6fe4e0feb87a3d32cf5bdf032e1044b0dbb6ef
