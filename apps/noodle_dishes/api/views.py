from rest_framework.viewsets import ModelViewSet

from apps.noodle_dishes.models import Noodle_dishes
from apps.noodle_dishes.api.serializers import Noodle_dishesSerializer

class Noodle_dishesApiViewSet(ModelViewSet):
    queryset = Noodle_dishes.objects.all()
    serializer_class = Noodle_dishesSerializer