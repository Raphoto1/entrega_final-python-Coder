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

from testing_core.views import (home, platform, 
                                TestPlatformCreateView, TestPlatformListView, TestPlatformDeleteView, TestPlatformUpdateView, TestPlatformDetailView, 
                                TestContextCreateView, TestContextListView, TestContextDeleteView, TestContextUpdateView, TestContextDetailView,
                                TestAppCreateView, TestAppListView, TestAppDeleteView, TestAppUpdateView, TestAppDetailView,
                                FakeUserCreateView, FakeUserListView, FakeUserDeleteView, FakeUserUpdateView, FakeUserDetailView,
                                QuestionCreateView, QuestionListView, QuestionDeleteView, QuestionUpdateView, QuestionDetailView, QuestionDetailView,
)

urlpatterns = [
    path('', home, name='home'),
    path('platform/', platform, name='platform'),
    # Platforms
    path('createPlatform/', TestPlatformCreateView.as_view(), name='create_platform'),
    path('listPlatforms/', TestPlatformListView.as_view(), name='list_platforms'),
    path('deletePlatform/<int:pk>/', TestPlatformDeleteView.as_view(), name='delete_platform'),
    path('updatePlatform/<int:pk>/', TestPlatformUpdateView.as_view(), name='update_platform'),
    path('detailPlatform/<int:pk>/', TestPlatformDetailView.as_view(), name='detail_platform'),
    # Contexts
    path('createContext/', TestContextCreateView.as_view(), name='create_context'),
    path('listContext/', TestContextListView.as_view(), name='list_contexts'),
    path('deleteContext/<int:pk>/', TestContextDeleteView.as_view(), name='delete_context'),
    path('updateContext/<int:pk>/', TestContextUpdateView.as_view(), name='update_context'),
    path('detailContext/<int:pk>/', TestContextDetailView.as_view(), name='detail_context'),
    # Apps
    path('createApp/', TestAppCreateView.as_view(), name='create_app'),
    path('listApps/', TestAppListView.as_view(), name='list_apps'),
    path('deleteApp/<int:pk>/', TestAppDeleteView.as_view(), name='delete_app'),
    path('updateApp/<int:pk>/', TestAppUpdateView.as_view(), name='update_app'),
    path('detailApp/<int:pk>/', TestAppDetailView.as_view(), name='detail_app'),
    # Fake Users
    path('createFakeUser/', FakeUserCreateView.as_view(), name='create_fake_user'),
    path('listFakeUsers/', FakeUserListView.as_view(), name='list_fake_users'),
    path('deleteFakeUser/<int:pk>/', FakeUserDeleteView.as_view(), name='delete_fake_user'),
    path('updateFakeUser/<int:pk>/', FakeUserUpdateView.as_view(), name='update_fake_user'),
    path('detailFakeUser/<int:pk>/', FakeUserDetailView.as_view(), name='detail_fake_user'),
    # Questions
    path('createQuestion/', QuestionCreateView.as_view(), name='create_question'),
    path('listQuestions/', QuestionListView.as_view(), name='list_questions'),
    path('deleteQuestion/<int:pk>/', QuestionDeleteView.as_view(), name='delete_question'),
    path('updateQuestion/<int:pk>/', QuestionUpdateView.as_view(), name='update_question'),
    path('detailQuestion/<int:pk>/', QuestionDetailView.as_view(), name='detail_question'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)