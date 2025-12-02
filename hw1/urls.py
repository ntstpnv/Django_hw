from django.urls import path

from hw1 import views


urlpatterns = [
    path("", views.HW1View.as_view(), name="hw1"),
    path("current_time/", views.CurrentTimeView.as_view(), name="current_time"),
    path("workdir/", views.WorkdirView.as_view(), name="workdir"),
]
