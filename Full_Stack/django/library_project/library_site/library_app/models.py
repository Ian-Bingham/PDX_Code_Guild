from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Borrower(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Book(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    checked_out = models.BooleanField(default=False)
    checkout_time = models.DateTimeField(null=True, blank=True)
    checkin_time = models.DateTimeField(auto_now_add=True)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
