from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='index'),
    # path('<int:question_id>/', views.detail, name='detail'),
    # path('<int:question_id>/results/', views.results, name='results'),
    # path('<int:question_id>/vote/', views.vote, name='vote'),

    path('<int:book_id>/', views.bookDetail, name='book_detail'),
    # path('<int:author_id>/', views.authorDetail, name='author_detail'),
]
