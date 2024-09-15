from django.shortcuts import render
from .models import Soups

def get_soups(request):
    soups = Soups.objects.all()
    return render (request, {'Soups': Soups})