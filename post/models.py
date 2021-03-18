from django.db import models

class Post(models.Model):
    text=models.TextField()
    author=models.CharField(max_length=40)
    title=models.CharField(max_length=250)
