from django.contrib import admin
from .models import Habit


@admin.register(Habit)
class HabitsAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "action",
        "place",
        "is_public",
    )
    list_filter = ("is_public",)
    search_fields = ("action",)
