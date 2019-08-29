from django.shortcuts import render
from .models import Foodtruck, Booth

# 푸드트럭 views.py
def foodtruck(request):
    foodtrucks = Foodtruck.objects.all()
    # print(foodtrucks.name)
    return render(request,'foodtruck.html',{'foodtrucks': foodtrucks})
