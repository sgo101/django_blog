from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_date = models.DateTimeField(auto_now=True)
    last_edit = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
