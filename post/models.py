from django.db import models
from django.urls import reverse
class Post(models.Model):
    text=models.TextField()
    author=models.CharField(max_length=40)
    title=models.CharField(max_length=250)

    def get_absolute_url(self):
        return reverse('home')
