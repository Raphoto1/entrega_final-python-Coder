
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from users.views import UserRegisterView, UserLoginView, test_view

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('test/', test_view, name='test')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)