from django.shortcuts import redirect

from base import views
from hw2.models import Dish


class HW2View(views.BaseTemplateView):
    objects = [
        {
            "title": "Показать список кулинарных рецептов",
            "path": "recipes",
        },
    ]
    back = "home"


class RecipeListView(views.BaseListView):
    template_name = "hw2/recipes.html"
    model = Dish
    paginate_by = 3

    title = "Список кулинарных рецептов"
    back = "hw2"

    def get(self, request, *args, **kwargs):
        request.session["page"] = request.GET.get("page", "1")

        return (
            super().get(request, *args, **kwargs)
            if request.GET.get("page")
            else redirect(f"{request.path}?page=1")
        )


class RecipeView(views.BaseDetailView):
    template_name = "hw2/recipe.html"
    queryset = Dish.objects.prefetch_related("recipe__ingredient__unit")

    back = "recipes"

    def get(self, request, *args, **kwargs):
        return (
            super().get(request, *args, **kwargs)
            if request.GET.get("servings")
            else redirect(f"{request.path}?servings=1")
        )

    def get_context_data(self, **kwargs):
        servings = int(self.request.GET.get("servings"))

        return {
            **super().get_context_data(**kwargs),
            "objects": [
                f"{dish.ingredient.name} - {dish.amount * servings} {dish.ingredient.unit.name}"
                for dish in self.object.recipe.all()
            ],
            "page": self.request.session.get("page"),
        }
