# Generated by Django 2.0.2 on 2018-04-01 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kotobjy', '0004_auto_20180401_0812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_books',
            name='review',
            field=models.TextField(default='', max_length=200, null=True),
        ),
    ]
