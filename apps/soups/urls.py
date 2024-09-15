from django.urls import path
from .views import get_soups

urlpatterns = [
    path('soups/', get_soups, name='get_soups'),
]