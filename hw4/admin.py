from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from hw4.models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main_count = 0
        for form in self.forms:
            if form.cleaned_data.get("is_main") and not form.cleaned_data.get(
                "DELETE", False
            ):
                main_count += 1

        if main_count == 0:
            raise ValidationError("Укажите основной раздел")
        if main_count > 1:
            raise ValidationError("Основным может быть только один раздел")


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    exclude = ["tags"]
    inlines = [ArticleTagInline]
    list_display = ["title", "published_at"]
    list_filter = ["published_at"]
    ordering = ["title"]
    search_fields = ["title", "published_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ["name"]
    ordering = ["name"]
    search_fields = ["name"]
