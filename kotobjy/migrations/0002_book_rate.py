# Generated by Django 2.0.2 on 2018-04-01 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotobjy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='rate',
            field=models.IntegerField(default=0),
        ),
    ]