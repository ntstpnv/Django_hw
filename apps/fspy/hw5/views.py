from django.conf import settings
from rest_framework import generics

from apps.menu import views
from . import serializers, models


class MenuView(views.MenuView):
    template_name = "hw5/sensors.html"
    queryset = None

    title = "Температурные датчики"
    back = "fspy"

    def get_queryset(self):
        return [
            settings.LINK("/api/measurements/", "measurements"),
            settings.LINK("/api/sensors/", "sensors"),
            *list(models.Sensor.objects.all()),
        ]


class MeasurementCreate(generics.CreateAPIView):
    http_method_names = ["post"]
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer


class SensorListAPIView(generics.ListCreateAPIView):
    http_method_names = ["get", "post"]
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorListSerializer


class SensorDetail(generics.RetrieveUpdateAPIView):
    http_method_names = ["get", "put"]
    queryset = models.Sensor.objects.prefetch_related("measurements")
    serializer_class = serializers.SensorDetailSerializer
