from django.urls import path
from hw1 import views


urlpatterns = [
    path("", views.home, name="home"),
    path("current_time/", views.current_time, name="current_time"),
    path("workdir/", views.workdir, name="workdir"),
]
