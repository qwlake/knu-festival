from django.shortcuts import render
from .models import Foodtruck, Booth, menu, booth_menu
from .forms import FoodtruckForm, BoothForm
from django.contrib.auth import authenticate
from django.contrib import auth
from django.shortcuts import render, redirect
from django.contrib import messages
import logging

# 푸드트럭 views.py
def foodtruck(request):
    foodtrucks = Foodtruck.objects.all().filter(divi=1)
    if len(foodtrucks)%2 == 0:
        foodtrucks1 = foodtrucks[:int(len(foodtrucks)/2)]
        foodtrucks2 = foodtrucks[int(len(foodtrucks)/2):]
    else:
        foodtrucks1 = foodtrucks[:int(len(foodtrucks)/2+1)]
        foodtrucks2 = foodtrucks[int(len(foodtrucks)/2+1):]
    
    return render(request,'foodtruck.html',{'foodtrucks1': foodtrucks1, 'foodtrucks2': foodtrucks2})

def haminseop(request):
    foodtrucks = Foodtruck.objects.all().filter(divi=2)
    booths = Booth.objects.all().filter(divi=2)
    # print(foodtrucks.name)
    return render(request,'haminseop.html',{'foodtrucks': foodtrucks, 'booths': booths})

def mirae(request):
    booths = Booth.objects.all().filter(divi=3)
    if len(booths)%2 == 0:
        booths1 = booths[:int(len(booths)/2)]
        booths2 = booths[int(len(booths)/2):]
    else:
        booths1 = booths[:int(len(booths)/2+1)]
        booths2 = booths[int(len(booths)/2+1):]
    # print(foodtrucks.name)
    return render(request,'mirae.html',{'booths1': booths1, 'booths2': booths2})

def login(request):
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is None:
            messages.error(request, '아이디 혹은 패스워드가 다릅니다.')
            return redirect('foodtruck:login')
        else:
            auth.login(request, user)
            try:
                foodtruck = Foodtruck.objects.get(user=user)
                return redirect('foodtruck:foodtruck_select', pk=foodtruck.id)
            except:
                booth = Booth.objects.get(user=user)
                return redirect('foodtruck:booth_select', pk=booth.id)

def foodtruck_select(request, pk):
    foodtruck = Foodtruck.objects.get(pk=pk)
    return render(request,'select.html', {'foodtruck': foodtruck})
    
def booth_select(request, pk):
    booth = Booth.objects.get(pk=pk)
    return render(request,'select.html', {'booth': booth})

def foodtruck_menu_list(request, pk):
    foodtruck = Foodtruck.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'menu.html', {'foodtruck': foodtruck})
    elif foodtruck.user == request.user:
        menu_context = {
            'foodtruck' : foodtruck,
            'food': request.POST['food'],
            'price': request.POST['price'],
        }
        newmenu = menu.objects.create(**menu_context)
        newmenu.save()
        messages.info(request, '메뉴를 추가했습니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=foodtruck.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=foodtruck.pk)

def foodtruck_menu_delete(request, pk):
    deleted_menu = menu.objects.get(pk=pk)
    foodtruck = deleted_menu.foodtruck
    if request.user == deleted_menu.foodtruck.user:
        deleted_menu.delete()
        messages.info(request, '삭제에 성공했습니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=foodtruck.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=foodtruck.pk)


def foodtruck_menu_update(request, pk):
    updated_menu = menu.objects.get(pk=pk)
    if request.user == updated_menu.foodtruck.user:
        updated_menu.food = request.POST['food']
        updated_menu.price = request.POST['price']
        updated_menu.save()
        messages.info(request, '수정에 성공했습니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=updated_menu.foodtruck.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:foodtruck_menu_list', pk=foodtruck.pk)

def foodtruck_update(request, pk):
    foodtruck = Foodtruck.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'updateFoodtruck.html',{'foodtruck': foodtruck})
    elif request.user == foodtruck.user:
        form = FoodtruckForm(request.POST, request.FILES, instance=foodtruck)
        if form.is_valid():
            form.save()
            messages.info(request, '수정에 성공했습니다!')
            return redirect('foodtruck:foodtruck_update', pk=foodtruck.id)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:foodtruck_update', pk=foodtruck.id)


def booth_menu_list(request, pk):
    booth = Booth.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'menu.html', {'booth': booth})
    elif booth.user == request.user:
        menu_context = {
            'booth' : booth,
            'food': request.POST['food'],
            'price': request.POST['price'],
        }
        newmenu = booth_menu.objects.create(**menu_context)
        messages.info(request, '메뉴를 추가했습니다')
        return redirect('foodtruck:booth_menu_list', pk=booth.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:booth_menu_list', pk=booth.pk)

def booth_menu_delete(request, pk):
    deleted_menu = booth_menu.objects.get(pk=pk)
    booth = deleted_menu.booth
    if request.user == deleted_menu.booth.user:
        deleted_menu.delete()
        messages.info(request, '삭제에 성공했습니다')
        return redirect('foodtruck:booth_menu_list', pk=booth.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:booth_menu_list', pk=booth.pk)

def booth_menu_update(request, pk):
    updated_menu = booth_menu.objects.get(pk=pk)
    if request.user == updated_menu.booth.user:
        updated_menu.food = request.POST['food']
        updated_menu.price = request.POST['price']
        updated_menu.save()
        messages.info(request, '수정에 성공했습니다')
        return redirect('foodtruck:booth_menu_list', pk=updated_menu.booth.pk)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:booth_menu_list', pk=updated_menu.booth.pk)

def booth_update(request, pk):
    booth = Booth.objects.get(pk=pk)
    if request.method == 'GET':
        return render(request,'updateBooth.html',{'booth': booth})
    elif request.user == booth.user:
        form = BoothForm(request.POST, request.FILES, instance=booth)
        if form.is_valid():
            form.save()
            messages.info(request, '수정에 성공했습니다!')
            return redirect('foodtruck:booth_update', pk=booth.id)
        else:
            messages.error(request, '서버 오류입니다')
            return redirect('foodtruck:booth_update', pk=booth.id)
    else:
        messages.error(request, '허용되지 않은 접근입니다.')
        return redirect('foodtruck:booth_update', pk=booth.id)

