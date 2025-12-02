from django.views.generic import DetailView, ListView, TemplateView


class BaseTemplateView(TemplateView):
    template_name = "base/menu.html"

    title = "Выберите задание"
    objects = []
    back = ""

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "objects": self.objects,
            "back_exists": bool(self.back),
            "back": self.back,
        }


class BaseListView(ListView):
    title = ""
    back = ""

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back": self.back,
        }


class BaseDetailView(DetailView):
    title = ""
    back = ""

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.title,
            "back": self.back,
        }
