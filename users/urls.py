
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from django.contrib.auth.views import LogoutView
from .views import UserRegisterView, UserLoginView, UserLogoutView, ProfileView, ProfileUpdateView, AvatarUpdateView, ProfileRoleView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('profile/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('avatar/update/', AvatarUpdateView.as_view(), name='avatar_update'),
    path('profile/role/', ProfileRoleView.as_view(), name='profile_role'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)