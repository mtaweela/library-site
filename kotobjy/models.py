from django.db import models


# Create your models here.


# Follow table used to track the authors from users
class Follow(models.Model):
    user_id = models.ForeignKey('auth_user', on_delete=models.CASCADE,)
    author_id = models.ForeignKey('author', on_delete=models.CASCADE,)


# books that readed by user
class User_books(models.Model):
    user_id = models.ForeignKey('auth_user', on_delete=models.CASCADE,)
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)
    rate = models.DecimalField(max_digits=1, decimal_places=1, default=0)
    review = models.TextField(max_length=200,)


# user wishlist
class User_wish_list(models.Model):
    user_id = models.ForeignKey('auth_user', on_delete=models.CASCADE,)
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)


# books owned by authors
class Author_books:
    book_id = models.ForeignKey('book', on_delete=models.CASCADE,)
    author_id = models.ForeignKey('author', on_delete=models.CASCADE,)

class Author(models.Model):
    name = models.CharField(max_length=200, null=Flase, required=True)
    pic = models.CharField(max_length=300)
    bio = models.CharField(max_length=2000)

class Book(models.Model):
    title = models.CharField(max_length=200, null=Flase, required=True)
    pic = models.CharField(max_length=300, null=Flase)
    describtion = models.CharField(max_length=2000)
    category = models.CharField(max_length=200, null=Flase)
    pub_date = models.DateTimeField('date published')

class Ex_user(models.Model):
    user_id = models.OneToOneField('auth_user', on_delete=models.CASCADE, primary_key=True, null=Flase)
    pic = models.CharField(max_length=300)


class User_fav(models.Model):
    user_id = models.ForeignKey('auth_user',on_delete=models.CASCADE)
    cat_name = models.CharField(max_length=200, null=Flase)

    class Meta:
        unique_together = (("user_id","cat_name"))
