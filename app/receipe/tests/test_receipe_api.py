from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Reciepe
from receipe.serializers import RecipeSerializer

RECEIPES_URL = reverse('receipe:receipe-list')

def sample_recipe(user, **params):
  """Create and return a sample receipe"""
  defaults = {
    "title":"Sample Receipe",
    "time_minutes": 10,
    "price":5
  }
  defaults.update(params)

  return receipe.objects.create(user = user, **defaults)

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
