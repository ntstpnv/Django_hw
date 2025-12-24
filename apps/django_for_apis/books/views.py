from apps.menu import views
from . import models


class BookListView(views.MenuView):
    template_name = "books/books.html"
    queryset = models.Book.objects.all()

    title = "All books"
    back = "django_for_apis"
