"""
URL configuration for manualtesting project.

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from testing_core.views import (TestPlatformCreateView, create_context, home, 
                                platform,
                                TestPlatformListView, TestPlatformDeleteView,
                                TestPlatformUpdateView, TestPlatformDetailView)

urlpatterns = [
    path('', home, name='home'),
    path('platform/', platform, name='platform'),
    path('createPlatform/', TestPlatformCreateView.as_view(), name='create_platform'),
    path('listPlatforms/', TestPlatformListView.as_view(), name='list_platforms'),
    path('deletePlatform/<int:pk>/', TestPlatformDeleteView.as_view(), name='delete_platform'),
    path('updatePlatform/<int:pk>/', TestPlatformUpdateView.as_view(), name='update_platform'),
    path('detailPlatform/<int:pk>/', TestPlatformDetailView.as_view(), name='detail_platform'),
    path('createContext/', create_context , name='create_context'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)