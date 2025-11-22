import csv

from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


DATA = {
    "omlet": {
        "title": "Омлет",
        "recipe": {
            "яйца, шт": 2,
            "молоко, л": 0.1,
            "соль, ч.л.": 0.5,
        },
    },
    "pasta": {
        "title": "Паста",
        "recipe": {
            "макароны, г": 0.3,
            "сыр, г": 0.05,
        },
    },
    "buter": {
        "title": "Бутерброд",
        "recipe": {
            "хлеб, ломтик": 1,
            "колбаса, ломтик": 1,
            "сыр, ломтик": 1,
            "помидор, ломтик": 1,
        },
    },
}


def hw2(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "menu.html",
        {
            "title": "Выберите задание",
            "pages": [
                {
                    "title": "Показать список рецептов",
                    "path": "get_recipes",
                },
                {
                    "title": "Показать список остановок",
                    "path": "get_stops",
                },
            ],
            "back": True,
            "path": "home",
        },
    )


def get_recipes(request: HttpRequest) -> HttpResponse:
    return render(
        request,
        "hw2/recipes.html",
        {
            "title": "Выберите блюдо",
            "recipes": [
                {"title": recipe["title"], "path": "get_recipe", "dish": dish}
                for dish, recipe in DATA.items()
            ],
            "path": "hw2",
        },
    )


def get_recipe(request: HttpRequest, dish: str) -> HttpResponse:
    recipe = DATA.get(dish, {})

    return render(
        request,
        "hw2/recipe.html",
        {
            "title": recipe.get("title", "Такого блюда не найдено"),
            "recipe": {
                k: v * int(request.GET.get("servings", "1"))
                for k, v in recipe.get("recipe").items()
            }
            if recipe
            else None,
            "path": "get_recipes",
        },
    )


def get_data() -> tuple[list[str], list[list[str]]]:
    with open("data-752-2025-11-05.csv", "r", encoding="utf-8") as file:
        reader = csv.reader(file, delimiter=";")

        _ = next(reader)

        headers = [header for i, header in enumerate(next(reader)) if i in (1, 6)]
        stops = [
            [value for i, value in enumerate(stop) if i in (1, 6)]
            for stop in list(reader)
        ]

        return headers, stops


HEADERS, STOPS = get_data()


def get_stops(request: HttpRequest) -> HttpResponse:
    stops = Paginator(STOPS, 10)

    return render(
        request,
        "hw2/stops.html",
        {
            "title": "Остановки наземного транспорта",
            "headers": HEADERS,
            "stops": stops.get_page(int(request.GET.get("page", "1"))),
            "path": "hw2",
        },
    )
