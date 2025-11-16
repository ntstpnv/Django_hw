from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def home(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "menu.html",
        {
            "title": "Выберите домашнее задание",
            "pages": [
                {
                    "title": "hw1",
                    "path": "hw1",
                },
                {
                    "title": "hw2",
                    "path": "hw2",
                },
            ],
            "back": False,
        },
    )
