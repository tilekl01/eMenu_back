from django.shortcuts import render
from .models import Drinks 

def get_drinks(request):
    drinks = Drinks.objects.all()
    return render(request, {'drinks': drinks})