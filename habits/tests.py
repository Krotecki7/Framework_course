from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from habits.models import Habit
from users.models import User


class HabitTestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create(email="test@test.com")
        self.habit = Habit.objects.create(
            place="парк", action="пробежка"
        )
        self.client.force_authenticate(user=self.user)

    def test_habit_retrieve(self):
        url = reverse("habits:habits-retrieve", args=(self.habit.pk,))
        response = self.client.get(url)
        data = response.json()
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("place"), self.habit.place)

    def test_habit_create(self):
        url = reverse("habits:habits-create")
        data = {"place": "парк", "action": "пробежка"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_habit_update(self):
        url = reverse("habits:habits-update", args=(self.habit.pk,))
        data = {"action": "Чтение"}
        response = self.client.patch(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data.get("action"), "Чтение")

    def test_habit_delete(self):
        url = reverse("habits:habits-delete", args=(self.habit.pk,))
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_habit_list(self):
        url = reverse("habits:habits-list")
        response = self.client.get(url)
        data = response.json()
        result = {
            "count": 1,
            "next": None,
            "previous": None,
            "results": [
                {
                    "id": self.habit.pk,
                    "time_to_complete": self.habit.time_to_complete,
                    "place": self.habit.place,
                    "time": self.habit.time,
                    "action": self.habit.action,
                    "pleasure_habit": self.habit.pleasure_habit,
                    "period": self.habit.period,
                    "reward": self.habit.reward,
                    "user": self.habit.user,
                    "related_habit": self.habit.related_habit,
                }
            ],
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(data, result)
