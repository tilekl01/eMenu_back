from rest_framework.routers import DefaultRouter

from apps.noodle_dishes.api.views import Noodle_dishesApiViewSet

router = DefaultRouter()
router.register(
    r'noodle_dishes',
    Noodle_dishesApiViewSet
)

urlpatterns = router.urls