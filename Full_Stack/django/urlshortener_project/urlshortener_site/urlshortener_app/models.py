from django.db import models


# Create your models here.
class URL(models.Model):
    og_url = models.CharField(max_length=500, unique=True)
    short_url = models.CharField(max_length=100, unique=True)
    url_tag = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.og_url
