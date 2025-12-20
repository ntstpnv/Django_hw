from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from debug_toolbar.toolbar import debug_toolbar_urls

from base import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", views.BaseListView.as_view(), name="home"),
    path("hw1/", include("hw1.urls")),
    path("hw2/", include("hw2.urls")),
    path("hw3/", include("hw3.urls")),
    path("hw4/", include("hw4.urls")),
    path("hw5/", include("hw5.urls")),
    path("hw6/", include("hw6.urls")),
    # path("hw7/api/", include("hw7.urls.py")),
    *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    *(debug_toolbar_urls() if settings.DEBUG else []),
]
