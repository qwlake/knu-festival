from django.shortcuts import render
from .models import Foodtruck, Booth
from django.contrib.auth import authenticate
# 푸드트럭 views.py
def foodtruck(request):
    foodtrucks = Foodtruck.objects.all()
    # print(foodtrucks.name)
    return render(request,'foodtruck.html',{'foodtrucks': foodtrucks})

def login(request):
    user = request.POST['user']
    password = request.POST['password']
    user = authenticate(username=user, password=password)
    
    if user is not None:
        messages.error(request, '패스워드가 다릅니다.')
        return redirect('/foodtruck/' + str(foodtruck.id))
    else:
        try:
            foodtruck = Foodtruck.objects.get(user=user)
            return redirect('/foodtruck/' + str(foodtruck.id))
        except:
            booth = Booth.objects.get(user=user)
            return redirect('/booth/' + str(booth.id))

def foodtruck_update(request, pk):
    foodtruck = Foodtruck.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'updateFoodtruck.html',{'foodtruck': foodtruck})
    else:
        foodtruck.name = request.POST['name']
        foodtruck.memo = request.POST['memo']
        foodtruck.image = request.POST['image']
        return redirect('/')

def booth_update(request, pk):
    if request.method == 'GET':
        booth = Booth.objects.get(pk=pk)
        return render(request,'updateFoodtruck.html',{'booth': booth})
    else:
        foodtruck.name = request.POST['name']
        foodtruck.memo = request.POST['memo']
        foodtruck.image = request.POST['image']
        return redirect('/')

    # else:
    #     foodtruck = Foodtruck.objects.get(pk=pk)
    #     return render(request,'foodtruck.html',{'foodtrucks': foodtrucks})