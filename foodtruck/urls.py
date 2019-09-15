from django.urls import path
from . import views

# 푸드트럭 urls.py
app_name = 'foodtruck'
urlpatterns = [
    path('', views.foodtruck, name="foodtruck"),
    path('haminseop', views.haminseop, name="haminseop"),
    path('mirae', views.mirae, name="mirae"),
    
    path('booth/<int:pk>/select', views.booth_select, name="booth_select"),
    path('booth/<int:pk>', views.booth_update, name="booth_update"),
    path('booth/<int:pk>/menu', views.booth_menu_list, name="booth_menu_list"), 
    path('booth_menu/<int:pk>/delete', views.booth_menu_delete, name="booth_menu_delete"),
    path('booth_menu/<int:pk>/update', views.booth_menu_update, name="booth_menu_update"),   
    
    path('<int:pk>/select', views.foodtruck_select, name="foodtruck_select"),
    path('<int:pk>', views.foodtruck_update, name="foodtruck_update"),
    path('<int:pk>/menu', views.foodtruck_menu_list, name="foodtruck_menu_list"),
    path('menu/<int:pk>/delete', views.foodtruck_menu_delete, name="foodtruck_menu_delete"),
    path('menu/<int:pk>/update', views.foodtruck_menu_update, name="foodtruck_menu_update"),
    
    path('login', views.login, name="login"),
]
