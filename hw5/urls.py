from django.urls import path

from hw5 import views


urlpatterns = [
    path("", views.HW5View.as_view(), name="hw5"),
    path("api/measurements/", views.MeasurementCreate.as_view(), name="measurements"),
    path("api/sensors/", views.SensorListAPIView.as_view(), name="sensors"),
    path("api/sensors/<int:pk>/", views.SensorDetail.as_view(), name="sensor"),
]
