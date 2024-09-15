from rest_framework.serializers import ModelSerializer

from apps.drinks.models import Drinks


class DrinksSerializer(ModelSerializer):
    class Meta:
        model = Drinks
        fields = [
            "id",
            "title",
            "price",
            "currency",
            "is_active",
        ]