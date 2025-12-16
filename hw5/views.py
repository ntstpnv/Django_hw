from rest_framework import generics

from base import views
from hw5 import models, serializers


class HW5View(views.BaseListView):
    template_name = "hw5/sensors.html"
    queryset = None

    title = "Температурные датчики"
    back = "home"

    def get_queryset(self):
        return [
            {
                "title": "/hw5/api/measurements/",
                "path": "measurements",
            },
            {
                "title": "/hw5/api/sensors/",
                "path": "sensors",
            },
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
