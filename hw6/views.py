from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.viewsets import ModelViewSet

from hw6 import models, serializers


class ProductViewSet(ModelViewSet):
    queryset = models.Product.objects.all()
    serializer_class = serializers.ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ["title", "description"]
    pagination_class = PageNumberPagination


class StockViewSet(ModelViewSet):
    queryset = models.Stock.objects.all()
    serializer_class = serializers.StockSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filterset_fields = ["products"]
    search_fields = ["address", "products__title", "products__description"]
    pagination_class = PageNumberPagination
