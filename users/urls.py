
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from .views import UserRegisterView, UserLoginView, UserLogoutView, ProfileView, ProfileUpdateView, AvatarUpdateView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', UserLogoutView.as_view(), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('avatar/update/', AvatarUpdateView.as_view(), name='avatar_update'),
]