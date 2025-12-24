from django.conf import settings

from apps.base import views
from . import consts


class MenuView(views.BaseMenuView):
    queryset = settings.APPS[consts.GROUP]

    back = "home"
