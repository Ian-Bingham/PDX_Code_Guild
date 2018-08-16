from django.db import models
from datetime import datetime


# Create your models here.
class Todo(models.Model):
    todo_text = models.CharField(max_length=200, unique=True)
    completed = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.todo_text
