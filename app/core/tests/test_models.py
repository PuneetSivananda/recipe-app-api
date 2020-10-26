from django.test import TestCase
from django.contrib.auth import get_user_model

from core import models


def sample_user(email="test@example.com", password="test"):
    """Create a simple user"""
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        '''Test Creating a new user with a email is successful'''
        email = 'test.user@gmail.com'
        password = 'testUser'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        '''Test the email for a new user is normalized'''
        email = 'test@TESTAPPDEV.com'
        user = get_user_model().objects.create_user(email, 'test123')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test Creating a no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test Creating a new super user"""
        user = get_user_model().objects.create_superuser(
            'user@superuser.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """Test the string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name="Vegan"
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredients_str(self):
        """Test the ingrediant string representation"""
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name="Cucumber"
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_receipe_str(self):
        """Test the receipe string representation"""
        receipe = models.Receipe.objects.create(
            user=sample_user(),
            title="Steak and Mushsroom sauce",
            time_minutes=5,
            price=5.00
        )

        self.assertEqual(str(receipe), receipe.title)
