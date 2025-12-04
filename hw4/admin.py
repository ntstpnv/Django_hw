from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from hw4.models import Article, Tag, ArticleTag


class ArticleTagInlineFormset(BaseInlineFormSet):
    def clean(self):
        super().clean()
        main = sum(
            not form.cleaned_data.get("DELETE", False)
            and form.cleaned_data.get("is_main", False)
            for form in self.forms
        )

        if not main:
            raise ValidationError("Укажите основной раздел")
        elif main > 1:
            raise ValidationError("Основным может быть только один раздел")


class ArticleTagInline(admin.TabularInline):
    model = ArticleTag
    formset = ArticleTagInlineFormset
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ArticleTagInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass
