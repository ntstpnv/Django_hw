from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40, unique=True)
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=160, unique=True)
    release_date = models.DateField()
    lte_exists = models.BooleanField()
    slug = models.SlugField(max_length=40, unique=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
