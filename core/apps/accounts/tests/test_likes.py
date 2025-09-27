from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient

from core.apps.accounts.models import LikesModel


class LikesTest(TestCase):

    def _create_data(self):
        return LikesModel._create_fake()

    def setUp(self):
        self.client = APIClient()
        self.instance = self._create_data()
        self.client.force_authenticate(user=self.instance.user)
        self.urls = {
            "list": reverse("likes-list"),
            "detail": reverse("likes-detail", args=[self.instance.id]),
        }

    def test_create(self):
        response = self.client.post(
            self.urls["list"],
            data={"ticket": LikesModel._create_fake().ticket.id},
        )
        self.assertEqual(response.status_code, 201)
        self.assertTrue(response.json()["status"])

    def test_destroy(self):
        response = self.client.delete(self.urls["detail"])
        self.assertEqual(response.status_code, 204)

    def test_list(self):
        response = self.client.get(self.urls["list"])
        self.assertTrue(response.json()["status"])
        self.assertEqual(response.status_code, 200)
