from django.shortcuts import render
from .models import Foodtruck, Booth

# 푸드트럭 views.py
def foodtruck(request):
    foodtrucks = Foodtruck.objects.all()
    foodtrucks1 = foodtrucks[:int(len(foodtrucks)/2+1)]
    foodtrucks2 = foodtrucks[int(len(foodtrucks)/2+1):]
    # print(foodtrucks.name)
    return render(request,'foodtruck.html',{'foodtrucks1': foodtrucks1, 'foodtrucks2': foodtrucks2})

def haminseop(request):
    booths = Booth.objects.all()
    booths1 = booths[:int(len(booths)/2+1)]
    booths2 = booths[int(len(booths)/2+1):]
    # print(foodtrucks.name)
    return render(request,'haminseop.html',{'booths1': booths1, 'booths2': booths2})

def mirae(request):
    booths = Booth.objects.all()
    booths1 = booths[:int(len(booths)/2+1)]
    booths2 = booths[int(len(booths)/2+1):]
    # print(foodtrucks.name)
    return render(request,'haminseop.html',{'booths1': booths1, 'booths2': booths2})