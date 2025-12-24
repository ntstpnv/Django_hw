from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.CharField(max_length=256)
    author = models.CharField(max_length=128)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]
