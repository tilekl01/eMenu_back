from rest_framework.serializers import ModelSerializer

from apps.noodle_dishes.models import Noodle_dishes


class Noodle_dishesSerializer(ModelSerializer):
    class Meta:
        model = Noodle_dishes
        fields = [
            "id",
            "image",
            "description",
            "title",
            "price",
            "currency",
            "is_active",
        ]