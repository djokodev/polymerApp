"""
URL configuration for polymereProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework.routers import DefaultRouter
from polymere.views import HealthCheck, Polymers, ReactedPolymer
from rest_framework.authtoken import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path("health_check/", HealthCheck.as_view(), name="health_check"),
    path("polymers/", Polymers.as_view({'get': 'list', 'post': 'create'}), name="polymers"),
    path("reactor/",ReactedPolymer.as_view({'get': 'list'}), name="reactor"),
    path("api-auth/", include("rest_framework.urls")),
    path('api-token-auth/', views.obtain_auth_token, name="api-token-auth")
]
