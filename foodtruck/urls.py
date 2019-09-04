from django.urls import path
from . import views

# 푸드트럭 urls.py
app_name = 'foodtruck'
urlpatterns = [
    path('', views.foodtruck, name="foodtruck"),
    path('haminseop', views.haminseop, name="haminseop"),
    path('mirae', views.mirae, name="mirae"),
    path('<int:pk>', views.foodtruck_update, name="foodtruck_update"),
    path('booth/<int:pk>', views.booth_update, name="booth_update"),
    path('login', views.login, name="login"),
]
