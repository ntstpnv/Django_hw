from rest_framework import serializers

from hw5 import models


class MeasurementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Measurement
        fields = ["sensor", "temperature", "image", "created_at"]


class SensorListSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Sensor
        fields = "__all__"


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(many=True, read_only=True)

    class Meta:
        model = models.Sensor
        fields = ["id", "name", "description", "measurements"]
