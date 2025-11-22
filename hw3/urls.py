from django.urls import path

from hw3 import views


urlpatterns = [
    path("", views.hw3, name="hw3"),
    path("catalog/", views.get_phones, name="get_phones"),
    path("catalog/<slug:phone>/", views.get_phone, name="get_phone"),
]
