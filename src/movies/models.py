from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=120)
    author = models.CharField(max_length=64)
    content = models.TextField()
    # created_on = models.DateField("Created on", default=timezone.now)

    def __str__(self):
        return self.title
