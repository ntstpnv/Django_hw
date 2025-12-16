from django.shortcuts import redirect

from base import views
from hw3 import models


class HW3View(views.BaseListView):
    queryset = [
        {
            "title": "Показать каталог смартфонов",
            "path": "phones",
        },
    ]

    back = "home"


class PhoneListView(views.BaseListView):
    template_name = "hw3/phones.html"
    queryset = None

    title = "Каталог смартфонов"
    back = "hw3"

    def get(self, request, *args, **kwargs):
        request.session["sort"] = request.GET.get("sort", "name")

        return (
            super().get(request, *args, **kwargs)
            if request.GET.get("sort")
            else redirect(f"{request.path}?sort=name")
        )

    def get_queryset(self):
        return models.Phone.objects.all().order_by(self.request.GET.get("sort"))


class PhoneView(views.BaseDetailView):
    template_name = "hw3/phone.html"

    back = "phones"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "title": self.object.name,
            "sort": self.request.session.get("sort"),
        }

    def get_object(self, queryset=None):
        return models.Phone.objects.get(slug=self.kwargs.get("slug"))
