from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Tag, Ingredient

from receipe import serializers


class BaseReceipeAttrViewSet(viewsets.GenericViewSet,
                             mixins.ListModelMixin,
                             mixins.CreateModelMixin
                             ):
    """Base viewset for user owned receipe attributes"""
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        """ Return objects for current authenticated user only"""
        return self.queryset.filter(user=self.request.user).order_by('-name')

    def perform_create(self, serializer):
        """create a new object"""
        serializer.save(user=self.request.user)


class TagViewSet(BaseReceipeAttrViewSet
                 ):
    """Manage Tags in the Database"""
    queryset = Tag.objects.all()
    serializer_class = serializers.TagSerializer


class IngredientViewSet(BaseReceipeAttrViewSet
                        ):
    """Manage Ingredients in the Database"""
    queryset = Ingredient.objects.all()
    serializer_class = serializers.IngredientSerializer
