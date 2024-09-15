from django.urls import path 
from .views import get_main_courses

urlpatterns = [ 
    path('main_courses/', get_main_courses, name='get_main_courses'), 
]