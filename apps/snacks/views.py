from django.shortcuts import render
from .models import Snacks 

def get_snacks (request):
    snacks = Snacks.objects.all()
    return render(request, {'snacks': snacks})