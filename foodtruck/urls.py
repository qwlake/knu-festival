from django.urls import path
from . import views

# 푸드트럭 urls.py
app_name = 'foodtruck'
urlpatterns = [
    path('', views.foodtruck, name="foodtruck"),
]
