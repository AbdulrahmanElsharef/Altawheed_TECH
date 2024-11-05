from django.shortcuts import render
from .models import *
# Create your views here.
def car_list(request):
    cars=Car.objects.all()
    
    context={"cars":cars,}
    return render(request, "Cars.html",context)