# admin password: qwer1234
# ahmed password: qwer1234
from django.contrib import admin
from .models import Book, Author, Ex_user

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Ex_user)
