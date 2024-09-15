from rest_framework.viewsets import ModelViewSet

from apps.main_courses.models import Main_courses
from apps.main_courses.api.serializers import Main_coursesSerializer

class Main_coursesApiViewSet(ModelViewSet):
    queryset = Main_courses.objects.all()
    serializer_class = Main_coursesSerializer