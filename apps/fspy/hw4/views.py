from django.conf import settings

from apps.base import views
from . import models


class MenuView(views.BaseMenuView):
    queryset = [
        settings.ITEM("Показать инфоцыганские курсы", "courses"),
        settings.ITEM("Показать новостные статьи", "articles"),
    ]

    back = "fspy"


class CourseView(views.BaseMenuView):
    template_name = "hw4/courses.html"
    queryset = models.DBManager.get_courses()

    title = "Инфоцыганские курсы"
    back = "hw4"

    def get(self, request, *args, **kwargs):
        if "generate" in request.GET:
            models.DBManager().generate()
        return super().get(request, *args, **kwargs)


class ArticleView(views.BaseMenuView):
    template_name = "hw4/news.html"
    queryset = models.DBManager.get_articles()

    back = "hw4"
