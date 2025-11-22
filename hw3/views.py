from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from hw3.models import Phone


def hw3(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "menu.html",
        {
            "title": "Выберите задание",
            "pages": [
                {
                    "title": "Показать каталог смартфонов",
                    "path": "get_phones",
                },
                # {
                #     "title": "",
                #     "path": "",
                # },
            ],
            "back": True,
            "path": "home",
        },
    )


def get_phones(request: HttpRequest) -> HttpResponse:
    phones = Phone.objects.all().order_by(request.GET.get("sort", "id"))

    return render(
        request,
        "hw3/phones.html",
        {
            "title": "Смартфоны",
            "phones": phones,
            "path": "hw3",
        },
    )


def get_phone(request: HttpRequest, phone: str) -> HttpResponse:
    phone = Phone.objects.get(slug=phone)

    return render(
        request,
        "hw3/phone.html",
        {
            "title": phone.name,
            "phone": phone,
            "path": "get_phones",
        },
    )
