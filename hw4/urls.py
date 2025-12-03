from django.urls import path

from hw4 import views


urlpatterns = [
    path("", views.HW4View.as_view(), name="hw4"),
    path("courses/", views.CourseView.as_view(), name="courses"),
    path("articles/", views.ArticleView.as_view(), name="articles"),
]
