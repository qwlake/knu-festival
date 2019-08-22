from django.shortcuts import render

# 푸드트럭 views.py
def foodtruck(request):
    return render(request,'foodtruck.html')
