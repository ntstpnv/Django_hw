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
                # {
                #     "title": "Показать список остановок",
                #     "path": "get_stops",
                # },
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


def get_stops(request: HttpRequest) -> HttpResponse:
    pass