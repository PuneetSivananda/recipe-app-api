from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Receipe
from receipe.serializers import RecipeSerializer

RECEIPES_URL = reverse('receipe:receipe-list')


def sample_recipe(user, **params):
    """Create and return a sample receipe"""
    defaults = {
        "title": "Sample Receipe",
        "time_minutes": 10,
        "price": 5
    }
    defaults.update(params)

    return receipe.objects.create(user=user, **defaults)


class PublicReceipeApiTests(TestCase):
    """Test Un authorized receipe API access"""

    def setup(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test that the authentication is required"""
        res = self.client.get(RECEIPES_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateReceipeApiTests(TestCase):
    """Test Unauthorized receipe api access"""

    def setup(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            'test@testuser.com',
            'testpass'
        )
        self.client.force_authenticate(self.user)

    def test_retrieve_receipes(self):
        """Test retreving a list of receipes"""
        sample_recipe(user=self.user)
        sample_recipe(user=self.user)

        res = self.client.get(RECEIPES_URL)

        receipes = receipes.object.all().order_by('-id')
        serializer = RecipeSerializer(receipes, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_receipes_limited_to_user(self):
        """Test retreving a receipes for user"""
        user2 = self.user = get_user_model().objects.create_user(
            'other@testuser.com',
            'testpass'
        )
        sample_recipe(user=user2)
        sample_recipe(user=self.user)

        res = self.client.get(RECEIPES_URL)
        receipes = receipes.object.filter(user=self.user)
        serializer = RecipeSerializer(receipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data, serializer.data)
