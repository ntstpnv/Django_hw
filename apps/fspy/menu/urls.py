from django.conf import settings
from django.urls import include, path

from . import consts, views


urlpatterns = [
    path("", views.MenuView.as_view(), name=consts.GROUP),
    *[
        path(f"{item.path}/", include(f"apps.{consts.GROUP}.{item.path}.urls"))
        for item in settings.APPS[consts.GROUP]
    ],
]
