from django.shortcuts import redirect

from base import views
from hw3.models import Phone


class HW3View(views.BaseTemplateView):
    objects = [
        {
            "title": "Показать каталог смартфонов",
            "path": "phones",
        },
    ]
    back = "home"


class PhoneListView(views.BaseListView):
    template_name = "hw3/phones.html"

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
        return Phone.objects.all().order_by(self.request.GET.get("sort", "id"))


class PhoneView(views.BaseDetailView):
    template_name = "hw3/phone.html"

    back = "phones"

    def get_context_data(self, **kwargs):
        return {
            **super().get_context_data(**kwargs),
            "sort": self.request.session.get("sort"),
        }

    def get_object(self, queryset=None):
        return Phone.objects.get(slug=self.kwargs.get("slug"))
