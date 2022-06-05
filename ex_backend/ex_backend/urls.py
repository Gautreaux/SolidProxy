"""ex_backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from core.views import front, note, note_detail

from core.views import get_all_models, get_models_hash


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", front, name="front"),
    path("notes/", note, name="note"),
    path("notes/<int:pk>/", note_detail, name="detail"),

    path("swmodels/", get_all_models),
    path("swm_hash/", get_models_hash),
]