from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# 분실물 urls.py
app_name = 'lostboard'
urlpatterns = [
    path('', views.board, name="board"),
    path('createpost/', views.createpost, name="createpost"),
    path('<int:pk>/', views.detail, name="detail"),
    path('<int:pk>/createcomment/', views.createcomment, name="createcomment"),
    path('<int:pk>/deletepost/', views.deletepost, name="deletepost"),
    path('<str:found>/', views.board, name="board"), # '주웠어요', '잃어버렸어요'를 구분해주는 path. 마지막 줄에 넣어야 함. 
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)