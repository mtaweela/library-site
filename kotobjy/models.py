from django.db import models

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