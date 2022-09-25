"""lesson27 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ads.views import index, AdListView, AdDetailView, CategoryListView, CategoryDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index_ads'),
    path('ad/', AdListView.as_view(), name='ads_list_view'),
    path('ad/<int:pk>', AdDetailView.as_view(), name='ad_detail_view'),
    path('cat/', CategoryListView.as_view(), name='cat_list_view'),
    path('cat/<int:pk>', CategoryDetailView.as_view(), name='cat_detail_view'),
]
