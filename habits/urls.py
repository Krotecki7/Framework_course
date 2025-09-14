from django.urls import path

from habits.apps import HabitsConfig
from .views import (
    HabitCreateApiView,
    HabitListApiView,
    HabitUpdateApiView,
    HabitDestroyApiView,
    HabitRetrieveApiView,
    PublicHabitListApiView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("habits/", HabitListApiView.as_view(), name="habits-list"),
    path("habits/<int:pk>/", HabitRetrieveApiView.as_view(), name="habits-retrieve"),
    path(
        "habits/<int:pk>/delete/",
        HabitDestroyApiView.as_view(),
        name="habits-delete",
    ),
    path(
        "habits/<int:pk>/update/", HabitUpdateApiView.as_view(), name="habits-update"
    ),
    path("habits/create/", HabitCreateApiView.as_view(), name="habits-create"),
    path("habits/public/", PublicHabitListApiView.as_view(), name="public_habits_list")
]
