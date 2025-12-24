from django.conf import settings
from django.db import models


class Advertisement(models.Model):
    class StatusChoices(models.IntegerChoices):
        DRAFT = 0, "Черновик"
        ACTIVE = 1, "Активно"
        CLOSED = 2, "Закрыто"

    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, default="")
    creator = models.ForeignKey(
        settings.AUTH_USER_MODEL, models.CASCADE, "advertisements"
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    status = models.SmallIntegerField(
        default=StatusChoices.DRAFT,
        choices=StatusChoices,
    )

    def __str__(self):
        return self.title
