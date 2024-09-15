from django.urls import path
from .views import  get_salads

urlpatterns = [
    path('salads/', get_salads, name='get_salad'),
]