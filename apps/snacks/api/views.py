from rest_framework.viewsets import ModelViewSet

from apps.snacks.models import Snacks
from apps.snacks.api.serializers import SnacksSerializer

class SnacksApiViewSet(ModelViewSet):
    queryset = Snacks.objects.all()
    serializer_class = SnacksSerializer