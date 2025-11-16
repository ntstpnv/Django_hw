from os import listdir

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def hw1(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "menu.html",
        {
            "title": "Выберите задание",
            "pages": [
                {
                    "title": "Показать текущее время",
                    "path": "get_current_time",
                },
                {
                    "title": "Показать содержимое рабочей директории",
                    "path": "get_workdir",
                },
            ],
            "back": True,
            "path": "home",
        },
    )


def get_current_time(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw1/current_time.html",
        {
            "title": "Текущее время",
            "path": "hw1",
        },
    )


def get_workdir(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw1/workdir.html",
        {
            "title": "Рабочая директория",
            "files": listdir(),
            "path": "hw1",
        },
    )
