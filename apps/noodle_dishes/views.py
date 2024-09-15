from django.shortcuts import render
from .models import Noodle_dishes

def get_noodle_dishes(request):
    noodle_dishes = Noodle_dishes.objects.all()
    return render(request, {'noodle_dishes': noodle_dishes})