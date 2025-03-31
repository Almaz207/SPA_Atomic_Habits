from django.core.exceptions import ValidationError

from habits.services import week_days


class FrequencyValidators:
    """Валидатор периодичности выполнения действия"""

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        if len(week_days(value["frequency"])) < 1:
            raise ValidationError(
                f"Чтобы выработать привычку нужно выполнять действие не реже одного раза в неделю"
            )


class RelatedFieldsValidator:
    def __init__(self, pleasant_habit, associated_habit, reward):
        self.pleasant_habit = pleasant_habit
        self.associated_habit = associated_habit
        self.reward = reward

    """
    -pleasant habit - признак приятной привычки
    -associated habit - связанная привычка
    -reward - вознаграждение
    """

    def __call__(self, value):
        pleasant_habit = value.get(self.pleasant_habit)
        associated_habit = value.get(self.associated_habit)
        reward = value.get(self.reward)

        if associated_habit and reward:
            raise ValidationError(
                "Должно быть заполнено только одно поле associated_habit или reward"
            )

        if pleasant_habit:
            if reward or associated_habit:
                raise ValidationError(
                    "У приятной привычки не может быть вознаграждения или связанной привычки"
                )


class AssociatedHabitValidator:
    def __init__(self, associated_habit):
        self.associated_habit = associated_habit

    def __call__(self, value):
        habit = value.get(self.associated_habit)
        if habit:
            if not habit.pleasant_habit:
                raise ValidationError("Связанная привычка должна быть приятной")
