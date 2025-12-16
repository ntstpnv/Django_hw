from django.views import generic


class BaseListView(generic.ListView):
    template_name = "base/menu.html"
    queryset = [
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
        {
            "title": "Работа с ORM, 2 часть",
            "path": "hw4",
        },
        {
            "title": "Знакомство с API на примере Django REST framework",
            "path": "hw5",
        },
        # {
        #     "title": "CRUD в DRF",
        #     "path": "hw6",
        # },
        # {
        #     "title": "Разделение доступа в DRF",
        #     "path": "hw7",
        # },
    ]

    title = "Выберите задание"
    back = ""

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back_exists": bool(self.back),
            "back": self.back,
        }


class BaseDetailView(generic.DetailView):
    title = ""
    back = ""

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back": self.back,
        }
