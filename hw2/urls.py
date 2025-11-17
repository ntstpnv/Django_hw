from django.urls import path

from hw2 import views


urlpatterns = [
    path("", views.hw2, name="hw2"),
    path("recipes/", views.get_recipes, name="get_recipes"),
    path("recipes/<str:dish>/", views.get_recipe, name="get_recipe"),
    path("stops/", views.get_stops, name="get_stops"),
]
