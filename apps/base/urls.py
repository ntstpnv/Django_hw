from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from apps.base import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.BaseMenuView.as_view(), name="home"),
    *[
        path(f"{item.path}/", include(f"apps.{item.path}.menu.urls"))
        for item in settings.GROUPS
    ],
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *(debug_toolbar_urls() if settings.DEBUG else []),
]
