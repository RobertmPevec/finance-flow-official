"""
URL configuration for CORE project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from HOMEPAGE.views import homepage, register, index, login_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("dashboard/", homepage, name="homepage"), 
    path("register/", register, name="register"),
    path("login/", login_view, name="login"),  # Use your custom login view
    path("home/", index, name="index"),  # Reference the index view
    path('accounts/', include('allauth.urls')),
]