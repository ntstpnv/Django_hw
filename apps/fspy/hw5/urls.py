from django.urls import path

from . import views

urlpatterns = [
    path("", views.MenuView.as_view(), name="hw5"),
    path("api/measurements/", views.MeasurementCreate.as_view(), name="measurements"),
    path("api/sensors/", views.SensorListAPIView.as_view(), name="sensors"),
    path("api/sensors/<int:pk>/", views.SensorDetail.as_view(), name="sensor"),
]
