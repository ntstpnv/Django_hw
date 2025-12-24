import os

from django.conf import settings

from apps.base import views


class MenuView(views.BaseMenuView):
    queryset = [
        settings.ITEM("Показать текущее время", "current_time"),
        settings.ITEM("Показать рабочую директорию", "workdir"),
    ]

    back = "fspy"


class CurrentTimeView(views.BaseMenuView):
    template_name = "hw1/current_time.html"
    queryset = []

    title = "Текущее время"
    back = "hw1"


class WorkdirView(views.BaseMenuView):
    template_name = "hw1/workdir.html"
    queryset = os.listdir()

    title = "Рабочая директория"
    back = "hw1"
