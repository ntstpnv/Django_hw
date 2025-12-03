from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=40, unique=True)
    slug = models.SlugField(max_length=40, unique=True)
    release_date = models.DateField()
    price = models.PositiveIntegerField()
    image = models.URLField(max_length=160, unique=True)
    lte_exists = models.BooleanField()
