from typing import Any

from django.http import HttpRequest, HttpResponse
from django.views.generic import ListView, TemplateView

from hw4.models import DBManager


class HW4View(TemplateView):
    template_name = "menu.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        return {
            **super().get_context_data(**kwargs),
            "title": "Выберите задание",
            "pages": [
                {
                    "title": "Показать курсы",
                    "path": "get_courses",
                },
                {
                    "title": "Показать статьи",
                    "path": "get_articles",
                },
            ],
            "back": True,
            "path": "home",
        }


class CourseView(ListView):
    template_name = "hw4/courses.html"
    queryset = DBManager.get_courses()

    def get(self, request: HttpRequest, *args, **kwargs) -> HttpResponse:
        if "generate" in request.GET:
            DBManager().generate()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        return {
            **super().get_context_data(**kwargs),
            "title": "Инфоцыганские курсы",
            "path": "hw4",
        }


class ArticleView(ListView):
    template_name = "articles/news.html"
    queryset = DBManager.get_articles()
