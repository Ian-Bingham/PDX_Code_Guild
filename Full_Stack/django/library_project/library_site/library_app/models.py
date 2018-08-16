from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)

    def __str__(self):
        return self.title


# class Borrower(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     book = models.ForeignKey(Book, on_delete=models.CASCADE)
#     checkout_time = models.DateTimeField()
#     checkout_in = models.DateTimeField(null=True)
