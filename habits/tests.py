from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from habits.models import Habit
from users.models import CustomUser


class HabitTest(APITestCase):
    """
    Тестирование API для модели Habit
    """

    def setUp(self):
        self.user = CustomUser.objects.create(email="test@test.ru", username="Test")
        self.habit = Habit.objects.create(
            action="test полезная привычка",
            time="12:00",
            reward="test вознаграждение",
            frequency="1,2,3,4,5,6,7",
            owner=self.user,
        )
        self.client.force_authenticate(user=self.user)

    def test_list_habit(self):
        """
        Тест получения списка привычек
        """
        url = "http://localhost:8000/habit/my_habits/"
        response = self.client.get(url)

        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.id,
                    "place": None,
                    "time": "12:00:00",
                    "action": "test полезная привычка",
                    "pleasant_habit": False,
                    "frequency": "1,2,3,4,5,6,7",
                    "reward": "test вознаграждение",
                    "time_to_perform": 120,
                    "publicity": False,
                    "owner": self.user.pk,
                    "associated_habit": None,
                }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), result)

    def test_create_habit(self):
        """
        Тест создания привычки
        """
        url = reverse("habit:habit_create")
        data = {
            "action": "test1 полезная привычка",
            "reward": "test1 вознаграждение",
            "frequency": "1,2,3,4,5,6,7",
            "time": "12:00",
        }
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Habit.objects.count(), 2)

    def test_retrieve_habit(self):
        """
        Получение конкретной привычки
        """
        url = f"http://localhost:8000/habit/habit_retrieve/{self.habit.pk}/"

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.assertEqual(response.json()["action"], "test полезная привычка")

    def test_update_habit(self):
        """
        Тест на изменения привычки
        """
        url = f"http://localhost:8000/habit/habit_update/{self.habit.id}/"

        data = {
            "action": "test1 полезная привычка",
            "reward": "test вознаграждение",
            "frequency": "1,2,3,4,5,6",
        }

        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json()["action"],
            "test1 полезная привычка",
        )

    def test_delete_habit(self):
        """
        удаления привычки
        """
        url = f"http://localhost:8000/habit/habit_destroy/{self.habit.pk}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Habit.objects.count(), 0)

    def test_user_habits_list(self):
        """
        получения списка привычек
        """
        url = "http://localhost:8000/habit/"

        response = self.client.get(url)

        result = {
            "count": 0,
            "next": None,
            "previous": None,
            "results": [
                # {
                #     "id": 38,
                #     "place": None,
                #     "time": "12:00:00",
                #     "action": "test полезная привычка",
                #     "pleasant_habit": False,
                #     "frequency": "1,2,3,4,5,6,7",
                #     "reward": "test вознаграждение",
                #     "time_to_perform": 120,
                #     "publicity": True,
                #     "owner": 1,
                #     "associated_habit": None
                #
                # }
            ],
        }

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), result)
