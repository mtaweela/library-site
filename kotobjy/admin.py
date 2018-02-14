from django.contrib import admin
from .models import Book, Author, Author_books, User_books

admin.site.register(Book)
admin.site.register(Author)
# admin.site.register(Author_books)
# admin.site.register(User_books)
