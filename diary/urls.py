from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView  # Импортируем LogoutView

urlpatterns = [
    path('', views.index, name='index'),  # Главная страница
    path('add/', views.add_travel, name='add_travel'),  # Добавление путешествия
    path('travel/<int:pk>/', views.travel_detail, name='travel_detail'),  # Детали путешествия
    path('register/', views.register, name='register'),  # Регистрация пользователя
]