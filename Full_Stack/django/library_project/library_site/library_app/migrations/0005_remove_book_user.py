# Generated by Django 2.0 on 2018-08-16 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library_app', '0004_book_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='user',
        ),
    ]