from os import listdir

from base import views


class HW1View(views.BaseListView):
    queryset = [
        {
            "title": "Показать текущее время",
            "path": "current_time",
        },
        {
            "title": "Показать содержимое рабочей директории",
            "path": "workdir",
        },
    ]

    back = "home"


class CurrentTimeView(views.BaseListView):
    template_name = "hw1/current_time.html"

    title = "Текущее время"
    back = "hw1"


class WorkdirView(views.BaseListView):
    template_name = "hw1/workdir.html"
    queryset = listdir()

    title = "Рабочая директория"
    back = "hw1"
