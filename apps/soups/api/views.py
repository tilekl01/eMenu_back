from rest_framework.viewsets import ModelViewSet

from apps.soups.models import Soups
from apps.soups.api.serializers import SoupsSerializer

class SoupsApiViewSet(ModelViewSet):
    queryset = Soups.objects.all()
    serializer_class = SoupsSerializer