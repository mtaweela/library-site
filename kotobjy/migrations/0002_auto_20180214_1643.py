# Generated by Django 2.0 on 2018-02-14 16:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kotobjy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Author_books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kotobjy.Author')),
            ],
        ),
        migrations.AddField(
            model_name='author_books',
            name='book_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='kotobjy.Book'),
        ),
    ]
