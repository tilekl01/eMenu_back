from django.urls import path 
from .views import get_snacks

urlpatterns = [ 
    path('snacks/', get_snacks, name='get_snacks'), 
]