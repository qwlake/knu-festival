from django.urls import path
from . import views

# index urls.py
app_name = 'index'
urlpatterns = [
    path('', views.index, name='index'),
]
