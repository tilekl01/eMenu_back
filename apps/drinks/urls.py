from django.urls import path 
from .views import get_drinks

urlpatterns = [ 
    path('drinks/', get_drinks, name='get_drinks'), 
]