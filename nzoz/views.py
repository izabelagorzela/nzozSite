from django.shortcuts import render
from .models import *



def index(request):
    return render(request, 'nzoz/index.html')

def poradnia_psychologiczna(request):
    specialists = Specialist.objects.filter(clinic__name='Poradnia psychologiczna').order_by('surname')
    return render(request, 'nzoz/poradnia_psychologiczna.html', {'specialists': specialists} )

def poradnia_psychiatryczna(request):
    specialists = Specialist.objects.filter(clinic__name='Poradnia psychiatryczna').order_by('surname')
    return render(request, 'nzoz/poradnia_psychiatryczna.html', {'specialists': specialists} )

def rejestracja(request):
    schedules = Schedule.objects.filter(clinic__name='Rejestracja').order_by('day__id')
    return render(request, 'nzoz/rejestracja.html', {'schedules' : schedules})

def lokalizacja(request):
    return render(request, 'nzoz/lokalizacja.html')

