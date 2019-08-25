from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# 분실물 urls.py
app_name = 'lostboard'
urlpatterns = [
    path('', views.lostboard, name="lostboard"),
    path('createlost/', views.createlost, name="createlost"),
    path('<int:pk>/', views.detail, name="detail"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)