from django.urls import path

from django_for_apis.books import views


urlpatterns = [
    path("", views.HW1View.as_view(), name="django_for_apis"),
    # path("current_time/", views.CurrentTimeView.as_view(), name="current_time"),
    # path("workdir/", views.WorkdirView.as_view(), name="workdir"),
]
