from django.urls import path

from hw1 import views


urlpatterns = [
    path("", views.hw1, name="hw1"),
    path("current_time/", views.get_current_time, name="get_current_time"),
    path("workdir/", views.get_workdir, name="get_workdir"),
]
