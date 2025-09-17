from django.db import models
from users.models import User

from django.core.validators import MaxValueValidator
from datetime import timedelta


class Habit(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name="Пользователь",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    place = models.CharField(max_length=28, verbose_name="Место привычки")
    time = models.TimeField(
        verbose_name="Время для начала выполнения привычки", blank=True, null=True
    )
    action = models.CharField(
        max_length=100, verbose_name="действие, которое представляет собой привычка"
    )
    pleasure_habit = models.BooleanField(
        verbose_name="Является ли привычка приятной", blank=True, null=True
    )
    related_habit = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        verbose_name="Связанная привычка",
        blank=True,
        null=True,
    )
    period = models.PositiveSmallIntegerField(
        validators=[MaxValueValidator(7)],
        verbose_name="Периодичность выполнения привычки",
        default=1,
        blank=True,
        null=True,
    )
    reward = models.CharField(
        max_length=100,
        verbose_name="Вознаграждение за выполнение привычки",
        blank=True,
        null=True,
    )
    time_to_complete = models.DurationField(
        default=timedelta(seconds=120),
        verbose_name="Время на выполение привычки",
        blank=True,
        null=True,
    )
    is_public = models.BooleanField(
        verbose_name="Признак публичности", blank=True, null=True
    )

    class Meta:
        verbose_name = "Привычка"
        verbose_name_plural = "Привычки"

    def __str__(self):
        return f"{self.action}"
