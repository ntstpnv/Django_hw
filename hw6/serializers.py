from rest_framework import serializers

from . import models


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Product
        fields = ["id", "title", "description"]


class ProductPositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.StockProduct
        fields = ["product", "quantity", "price"]


class StockSerializer(serializers.ModelSerializer):
    positions = ProductPositionSerializer(many=True)

    class Meta:
        model = models.Stock
        fields = ["id", "address", "positions"]

    def create(self, validated_data):
        positions = validated_data.pop("positions")
        stock = super().create(validated_data)

        for position in positions:
            models.StockProduct.objects.create(
                stock=stock,
                product=position["product"],
                quantity=position["quantity"],
                price=position["price"],
            )

        return stock

    def update(self, instance, validated_data):
        positions = validated_data.pop("positions")
        stock = super().update(instance, validated_data)

        instance.positions.all().delete()

        for position in positions:
            models.StockProduct.objects.update_or_create(
                stock=stock,
                product=position["product"],
                defaults={"quantity": position["quantity"], "price": position["price"]},
            )

        return stock
