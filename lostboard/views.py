from django.shortcuts import render

# 분실물 views.py

def lostboard(request):
    return render(request,'lostboard.html')