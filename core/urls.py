"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from dashboard.views import home
from user_accounts.views import profile, register
from parser.views import upload_resume, import_linkedin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # 🔑 Auth views
    path('profile/', profile, name='profile'),
    path('register/', register, name='register'),
    path('upload/', upload_resume, name='upload_resume'),
    path('import_linkedin/', import_linkedin, name='import_linkedin'),
    path('', home, name='home'),
]