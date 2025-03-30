from rest_framework import status
from rest_framework.test import APITestCase
from users.models import CustomUser


class UserTest(APITestCase):
    """
    Тестирование API для модели User
    """

    def setUp(self):
        self.user = CustomUser.objects.create(
            email="test@test.ru", is_staff=True, is_superuser=True
        )
        self.client.force_authenticate(user=self.user)

    def test_create_user(self):
        """
        Тест создания нового пользователя
        """
        url = "http://localhost:8000/user/register/"
        data = {"email": "test1@test.ru", "password": "test", "username": "testUser"}
        response = self.client.post(url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(CustomUser.objects.count(), 2)

    def test_list_users(self):
        """
        Тест получения списка пользователей
        """
        url = "http://localhost:8000/user/list_user/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.json())
        self.assertEqual(response.json()[0]["email"], "test@test.ru")

    def test_retrieve_users(self):
        """
        Тест получения конкретного пользователя
        """
        url = f"http://localhost:8000/user/user_retrieve/{self.user.pk}/"
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["email"], "test@test.ru")

    def test_update_user(self):
        """
        Тест на изменения информации о пользователе
        """
        url = f"http://localhost:8000/user/user_update/{self.user.pk}/"
        data = {"email": "test1@test.ru"}
        response = self.client.patch(url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()["email"], "test1@test.ru")

    def test_delete_user(self):
        """
        Тест удаления пользователя
        """
        url = f"http://localhost:8000/user/user_destroy/{self.user.pk}/"
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(CustomUser.objects.count(), 0)
