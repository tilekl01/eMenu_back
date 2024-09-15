from rest_framework.serializers import ModelSerializer

from apps.snacks.models import Snacks


class SnacksSerializer(ModelSerializer):
    class Meta:
        model = Snacks
        fields = [
            "id",
            "image",
            "description",
            "title",
            "price",
            "currency",
            "is_active",
        ]