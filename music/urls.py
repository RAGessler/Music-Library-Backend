from django.urls import path
from . import views

urlpatterns = [
    path('', views.music_library),
    path('<int:pk>/', views.music_detail)
]