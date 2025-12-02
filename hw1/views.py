from os import listdir

from base import views


class HW1View(views.BaseTemplateView):
    objects = [
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


class CurrentTimeView(views.BaseTemplateView):
    template_name = "hw1/current_time.html"

    title = "Текущее время"
    back = "hw1"


class WorkdirView(views.BaseTemplateView):
    template_name = "hw1/workdir.html"

    title = "Рабочая директория"
    objects = listdir()
    back = "hw1"
