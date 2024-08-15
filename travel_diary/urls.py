from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),  # Подключение URL-ов вашего приложения
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),  # Страница входа
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),  # Страница выхода
]

# Настройка URL для обслуживания медиафайлов на этапе разработки
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
