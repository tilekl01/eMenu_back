from django.shortcuts import render
from .models import Main_courses

def get_main_courses(request):
    main_courses = Main_courses.objects.all()
    return render(request, {'main_courses': main_courses})