from rest_framework.routers import DefaultRouter

from apps.snacks.api.views import SnacksApiViewSet

router = DefaultRouter()
router.register(
    r'snacks',
    SnacksApiViewSet
)

urlpatterns = router.urls