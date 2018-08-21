from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class BlogPost(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    body = models.TextField(max_length=None)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=True)
    blogpost = models.ForeignKey(BlogPost, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(max_length=None)
    timestamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.body