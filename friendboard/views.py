from django.shortcuts import render

# 술친구 views.py

def friendboard(request):
    return render(request,'friendboard.html')
