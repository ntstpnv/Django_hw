from django.urls import path

from hw5 import views


urlpatterns = [
    path("", views.HW5View.as_view(), name="hw5"),
    path("sensors/", views.SensorListCreate.as_view(), name="sensors"),
    path("sensors/<int:pk>/", views.SensorDetail.as_view(), name="sensor"),
    path("measurements/", views.MeasurementCreate.as_view(), name="measurement"),
]
