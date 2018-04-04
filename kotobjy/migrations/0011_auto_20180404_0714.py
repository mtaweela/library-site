# Generated by Django 2.0.2 on 2018-04-04 07:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('kotobjy', '0010_auto_20180404_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='userrate',
            name='book',
            field=models.ManyToManyField(to='kotobjy.Book'),
        ),
        migrations.RemoveField(
            model_name='user_fav',
            name='user',
        ),
        migrations.AddField(
            model_name='user_fav',
            name='user',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.RemoveField(
            model_name='userrate',
            name='user',
        ),
        migrations.AddField(
            model_name='userrate',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
