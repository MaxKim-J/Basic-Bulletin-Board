"""django_prac4_0730front URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from article import views
from article.views import HomeView, UserCreateView, UserCreationDoneTV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', HomeView.as_view(), name='home'),
    path('article/', include('article.urls')),
    path('profile/', views.profile, name='profile'),

    # 인증 유알엘
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register', UserCreateView.as_view(), name='register'),
    path('accounts/register/done', UserCreationDoneTV.as_view(), name='register_done'),
]
