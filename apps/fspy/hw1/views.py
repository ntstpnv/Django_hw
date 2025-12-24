import os

from django.conf import settings

from apps.menu import views


class MenuView(views.MenuView):
    queryset = [
        settings.LINK("Показать текущее время", "current_time"),
        settings.LINK("Показать рабочую директорию", "workdir"),
    ]

    back = "fspy"


class CurrentTimeView(views.MenuView):
    template_name = "hw1/current_time.html"
    queryset = []

    title = "Текущее время"
    back = "hw1"


class WorkdirView(views.MenuView):
    template_name = "hw1/workdir.html"
    queryset = os.listdir()

    title = "Рабочая директория"
    back = "hw1"
