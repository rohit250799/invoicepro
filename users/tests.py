from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model, authenticate, login
from django.http import HttpResponse

User = get_user_model()

# Create your tests here.

class UserCreationTestCase(APITestCase):
    def setUp(self) -> None:
        self.create_url = reverse('user-create')

    def test_create_user(self):
        data = {
            "username": "john",
            "email": "john@example.com",
            "password": "secret_password",
            "user_country": "US",
            "user_currency": "USD",
            "user_plan": "FREE"
        }
        response = self.client.post(self.create_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(User.objects.count(), 1)
        user = User.objects.get()
        self.assertEqual(user.username, "john")
        self.assertEqual(user.email, "john@example.com")
        self.assertTrue(user.check_password("secret_password"))
        self.assertEqual(user.user_country, "US")
        self.assertEqual(user.user_currency, "USD")
        self.assertEqual(user.user_plan, "FREE")