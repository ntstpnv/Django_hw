from django.conf import settings
from django.views import generic


class MenuView(generic.ListView):
    template_name = "menu/menu.html"
    queryset = [settings.LINK(group, group) for group in settings.APPS]

    title = "Выберите задание"
    back = None

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back_exists": bool(self.back),
            "back": self.back,
        }


class BaseDetailView(generic.DetailView):
    title = None
    back = None

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back": self.back,
        }
