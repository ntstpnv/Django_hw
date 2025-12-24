from apps.menu import views


class HW1View(views.BaseListView):
    template_name = "hw1/current_time.html"

    title = "Текущее время"
    back = "home"
