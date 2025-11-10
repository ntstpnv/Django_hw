from os import listdir

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.urls import reverse


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw1/home.html",
        {
            "pages": {
                "Показать текущее время": reverse("current_time"),
                "Показать содержимое рабочей директории": reverse("workdir"),
            }
        },
    )


def current_time(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw1/current_time.html",
    )


def workdir(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw1/workdir.html",
        {
            "files": listdir(),
        },
    )
