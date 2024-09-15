from rest_framework.viewsets import ModelViewSet

from apps.drinks.models import Drinks
from apps.drinks.api.serializers import DrinksSerializer


class DrinksApiViewSet(ModelViewSet):
    queryset = Drinks.objects.all()
    serializer_class = DrinksSerializer