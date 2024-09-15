from rest_framework.serializers import ModelSerializer

from apps.salads.models import Salads


class SaladsSerializer(ModelSerializer):
    class Meta:
        model = Salads
        fields = [
            "id",
            "image",
            "description",
            "title",
            "price",
            "currency",
            "is_active",
        ]