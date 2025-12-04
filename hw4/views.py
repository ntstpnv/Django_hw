from hw4.models import DBManager
from base import views


class HW4View(views.BaseTemplateView):
    objects = [
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
    queryset = DBManager.get_courses()

    title = "Инфоцыганские курсы"
    back = "hw4"

    def get(self, request, *args, **kwargs):
        if "generate" in request.GET:
            DBManager().generate()
        return super().get(request, *args, **kwargs)


class ArticleView(views.BaseListView):
    template_name = "hw4/news.html"
    queryset = DBManager.get_articles()

    back = "hw4"
