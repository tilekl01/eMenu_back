from rest_framework.routers import DefaultRouter

from apps.main_courses.api.views import Main_coursesApiViewSet

router = DefaultRouter()
router.register(
    r'main_courses',
    Main_coursesApiViewSet
)

urlpatterns = router.urls