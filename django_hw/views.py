from base import views


class HomeView(views.BaseTemplateView):
    objects = [
        {
            "title": "Знакомство с Django. Подготовка и запуск проекта",
            "path": "hw1",
        },
        {
            "title": "Обработка запросов и шаблоны",
            "path": "hw2",
        },
        {
            "title": "Работа с ORM",
            "path": "hw3",
        },
        # {
        #     "title": "hw4",
        #     "path": "hw4",
        # },
    ]
