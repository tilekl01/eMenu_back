from django.urls import path
from .views import get_noodle_dishes

urlpatterns = [
    path('noodles_dishes/', get_noodle_dishes, name='get_noodle_dishes'),
]