from rest_framework.routers import DefaultRouter

from apps.drinks.api.views import DrinksApiViewSet

router = DefaultRouter()
router.register(
    r'drinks',
    DrinksApiViewSet
)

urlpatterns = router.urls