from django.core import validators
from django.db import models


class Stock(models.Model):
    address = models.CharField(max_length=256, unique=True)
    products = models.ManyToManyField("Product", "stocks", through="StockProduct")


class Product(models.Model):
    title = models.CharField(max_length=64, unique=True)
    description = models.TextField(blank=True, null=True)


class StockProduct(models.Model):
    stock = models.ForeignKey("Stock", models.CASCADE)
    product = models.ForeignKey("Product", models.CASCADE)

    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(
        max_digits=8, decimal_places=2, validators=[validators.MinValueValidator(0)]
    )

    class Meta:
        default_related_name = "positions"
