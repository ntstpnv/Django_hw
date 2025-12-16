from base import views
from hw4 import models


class HW4View(views.BaseListView):
    queryset = [
        {
            "title": "Показать список инфоцыганских курсов",
            "path": "courses",
        },
        {
            "title": "Показать новостные статьи",
            "path": "articles",
        },
    ]

    back = "home"


class CourseView(views.BaseListView):
    template_name = "hw4/courses.html"
    queryset = models.DBManager.get_courses()

    title = "Инфоцыганские курсы"
    back = "hw4"

    def get(self, request, *args, **kwargs):
        if "generate" in request.GET:
            models.DBManager().generate()
        return super().get(request, *args, **kwargs)


class ArticleView(views.BaseListView):
    template_name = "hw4/news.html"
    queryset = models.DBManager.get_articles()

    back = "hw4"
