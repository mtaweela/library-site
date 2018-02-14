# admin password: qwer1234
# admin mail: admin@admin.com
# ahmed password: qwer1234
from django.contrib import admin
from .models import Book, Author, Ex_user, User_books, Follow, User_wish_list, Author_books, User_fav

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Ex_user)
admin.site.register(User_books)
admin.site.register(Follow)
admin.site.register(User_wish_list)
admin.site.register(Author_books)
admin.site.register(User_fav)