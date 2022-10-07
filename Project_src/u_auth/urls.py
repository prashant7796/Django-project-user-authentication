from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.HomePage),
    path('register', views.Register, name="register"),
    path('login', views.LoginPage, name="login"),
    path('logout', views.LogoutPage, name="logout"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)