from django.core.validators import MaxValueValidator
from django.db import models
from users.models import CustomUser

"""Пользователь — создатель привычки.
Место — место, в котором необходимо выполнять привычку.
Время — время, когда необходимо выполнять привычку.
Действие — действие, которое представляет собой привычка.
Признак приятной привычки — привычка, которую можно привязать к выполнению полезной привычки.
Связанная привычка — привычка, которая связана с другой привычкой, важно указывать для полезных привычек, но не для приятных.
Периодичность (по умолчанию ежедневная) — периодичность выполнения привычки для напоминания в днях.
Вознаграждение — чем пользователь должен себя вознаградить после выполнения.
Время на выполнение — время, которое предположительно потратит пользователь на выполнение привычки.
Признак публичности — привычки можно публиковать в общий доступ, чтобы другие пользователи могли брать в пример чужие привычки."""

"""User — Пользователь
-place - Место
-time - Время
-action - Действие
-pleasant habit - признак приятной привычки
-associated habit - связанная привычка
-frequency - периодичность
-reward - вознаграждение
-time to perform - времяна выполнение
-publicity - признак публичности"""


class Habit(models.Model):
    owner = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="habits",
        verbose_name="пользователь",
        blank=True,
    )
    place = models.CharField(
        max_length=150, null=True, blank=True, verbose_name="место"
    )
    time = models.TimeField(verbose_name="время")
    action = models.CharField(max_length=150, verbose_name="действие")
    pleasant_habit = models.BooleanField(
        default=False, verbose_name="признак приятной привычки"
    )
    associated_habit = models.ForeignKey(
        "Habit",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name="приятная привычка",
    )
    frequency = models.CharField(
        default="1,2,3,4,5,6,7", max_length=30, verbose_name="периодичность"
    )
    reward = models.TextField(null=True, blank=True, verbose_name="вознаграждение")
    time_to_perform = models.PositiveSmallIntegerField(
        verbose_name="время выполнения",
        blank=True,
        null=True,
        validators=[MaxValueValidator(120)],
        default=120,
    )

    publicity = models.BooleanField(default=False, verbose_name="признак публичности")


class Meta:
    verbose_name = "Привычка"
    verbose_name_plural = "Привычки"


def __str__(self):
    return f"{self.action}"
