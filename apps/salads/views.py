from django.shortcuts import render
from .models import Salads

def get_salads(request):
    salads = Salads.objects.all()
    return render(request, {'salads': salads})