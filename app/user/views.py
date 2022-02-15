from rest_framework import generics

from user.serializers import UserSerializer


class CreateUserView(generics.CreateAPIView):
    """Craete a new user view"""
    serializer_class = UserSerializer
