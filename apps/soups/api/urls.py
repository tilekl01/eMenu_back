from rest_framework.routers import DefaultRouter

from apps.soups.api.views import SoupsApiViewSet

router = DefaultRouter()
router.register(
    r'soups',
    SoupsApiViewSet
)

urlpatterns = router.urls