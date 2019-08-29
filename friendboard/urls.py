from django.urls import path
from . import views

# 술친구 urls.py
app_name = 'friendboard'
urlpatterns = [
    path('create/', views.post_create, name="create"),
    path('<int:pk>/delete', views.post_delete, name="delete"),
    path('', views.friendboard, name="friendboard"),
    path('f/',views.friendboardDetail, name="friendboardDetail")
    
]