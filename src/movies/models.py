from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=64)
    content = models.TextField()

    def __str__(self):
        return self.title
