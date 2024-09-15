from rest_framework.serializers import ModelSerializer

from apps.main_courses.models import Main_courses


class Main_coursesSerializer(ModelSerializer):
    class Meta:
        model = Main_courses
        fields = [
            "id",
            "image",
            "description",
            "title",
            "price",
            "currency",
            "is_active",
        ]