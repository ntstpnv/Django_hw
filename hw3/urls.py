from django.urls import path

from hw3 import views


urlpatterns = [
    path("", views.HW3View.as_view(), name="hw3"),
    path("catalog/", views.PhoneListView.as_view(), name="phones"),
    path("catalog/<slug:slug>/", views.PhoneView.as_view(), name="phone"),
]
