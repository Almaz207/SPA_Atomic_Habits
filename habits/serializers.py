from rest_framework.serializers import ModelSerializer
from habits.validators import (
    FrequencyValidators,
    RelatedFieldsValidator,
    AssociatedHabitValidator,
)
from habits.models import Habit


class HabitSerializer(ModelSerializer):
    class Meta:
        model = Habit
        fields = "__all__"
        validators = [
            FrequencyValidators(field="frequency"),
            RelatedFieldsValidator(
                pleasant_habit="pleasant_habit",
                associated_habit="associated_habit",
                reward="reward",
            ),
            AssociatedHabitValidator(associated_habit="associated_habit"),
        ]
