from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('book/<int:book_id>/', views.bookDetail, name='book_detail'),
    path('author/<int:author_id>/', views.authorDetail, name='author_detail'),
    path('books/', views.BookListView.as_view(), name='book_list'),

    # path('<int:author_id>/', views.authorDetail, name='author_detail'),
]
