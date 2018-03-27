from django.db import models
from django.contrib.auth.models import User

# Follow table used to track the authors from users


class Follow(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    author_id = models.ForeignKey('author', on_delete=models.CASCADE)


# books that readed by user
class User_books(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)
    rate = models.DecimalField(max_digits=1, decimal_places=1, default=0)
    review = models.TextField(max_length=200,)


# user wishlist
class User_wish_list(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)


# books owned by authors
class Author_books(models.Model):
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)
    author_id = models.ForeignKey('author', on_delete=models.CASCADE,)


class Author(models.Model):
    name = models.CharField(max_length=200, null=False)
    pic = models.CharField(max_length=300)
    bio = models.CharField(max_length=2000)


class Book(models.Model):
    title = models.CharField(max_length=200, null=False)
    pic = models.CharField(max_length=300)
    describtion = models.CharField(max_length=2000)
    category = models.CharField(max_length=200, null=False)
    pub_date = models.DateField('date published')


class Ex_user(models.Model):
    user_id = models.OneToOneField(User, on_delete=models.CASCADE)
    pic = models.CharField(max_length=300)


class User_fav(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=200, null=False)