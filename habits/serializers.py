from rest_framework import serializers
from .models import Habit
from .validators import (FieldFillingValidator, RelatedHabitValidator,
                         execution_time_validator)


class HabitSerializer(serializers.ModelSerializer):
    time_to_complete = serializers.DurationField(
        validators=[execution_time_validator],
        required=False
    )

    class Meta:
        model = Habit
        exclude = ("is_public",)
        validators = [
            FieldFillingValidator(
                "reward",
                "related_habit",
                "pleasure_habit"
            ),
            RelatedHabitValidator("related_habit"),
        ]


class PublicHabitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = ["user", "action", "period"]
