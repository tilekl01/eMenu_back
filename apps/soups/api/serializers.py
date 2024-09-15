from rest_framework.serializers import ModelSerializer

from apps.soups.models import Soups


class SoupsSerializer(ModelSerializer):
    class Meta:
        model = Soups
        fields = [
            "id",
            "image",
            "description",
            "title",
            "price",
            "currency",
            "is_active",
        ]