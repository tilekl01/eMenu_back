from rest_framework.viewsets import ModelViewSet

from apps.salads.models import Salads
from apps.salads.api.serializers import SaladsSerializer

class SaladsApiViewSet(ModelViewSet):
    queryset = Salads.objects.all()
    serializer_class = SaladsSerializer