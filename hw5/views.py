from rest_framework import generics

from base import views
from hw5 import models, serializers


class HW5View(views.BaseTemplateView):
    objects = [
        {
            "title": "Показать sensors",
            "path": "sensors",
        },
        # {
        #     "title": "Показать sensor",
        #     "path": "sensor",
        # },
        {
            "title": "Показать measurement",
            "path": "measurement",
        },
    ]
    back = "home"


class SensorListCreate(generics.ListCreateAPIView):
    queryset = models.Sensor.objects.all()
    serializer_class = serializers.SensorListSerializer


class MeasurementCreate(generics.CreateAPIView):
    queryset = models.Measurement.objects.all()
    serializer_class = serializers.MeasurementSerializer


class SensorDetail(generics.RetrieveUpdateAPIView):
    queryset = models.Sensor.objects.prefetch_related("measurements")
    serializer_class = serializers.SensorDetailSerializer
