from django.urls import path

from habits.apps import HabitsConfig

from habits.views import (
    HabitCreateAPIView,
    MyHabitListAPIView,
    PublicHabitListAPIView,
    HabitRetrieveAPIView,
    HabitUpdateAPIView,
    HabitDestroyAPIView,
)

app_name = HabitsConfig.name

urlpatterns = [
    path("", PublicHabitListAPIView.as_view(), name="public_habits_list"),
    path("my_habits/", MyHabitListAPIView.as_view(), name="person_habits_list"),
    path("create_habit/", HabitCreateAPIView.as_view(), name="habit_create"),
    path(
        "habit_retrieve/<int:pk>/",
        HabitRetrieveAPIView.as_view(),
        name="habit_retrieve",
    ),
    path("habit_update/<int:pk>/", HabitUpdateAPIView.as_view(), name="habit_update"),
    path(
        "habit_destroy/<int:pk>/", HabitDestroyAPIView.as_view(), name="habit_destroy"
    ),
]
# urlpatterns += router.urls
