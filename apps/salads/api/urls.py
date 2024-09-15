from rest_framework.routers import DefaultRouter

from apps.salads.api.views import SaladsApiViewSet

router = DefaultRouter()
router.register(
    r'salads',
    SaladsApiViewSet
)

urlpatterns = router.urls