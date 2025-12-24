from django.conf import settings
from django.views import generic


class BaseMenuView(generic.ListView):
    template_name = "base/menu.html"
    queryset = settings.GROUPS

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
