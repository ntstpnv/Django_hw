from django.contrib import admin

from hw2.models import Dish, Ingredient, Unit, Recipe


class RecipeInline(admin.TabularInline):
    model = Recipe
    extra = 1


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}

    inlines = [RecipeInline]


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    pass


@admin.register(Unit)
class UnitAdmin(admin.ModelAdmin):
    pass
