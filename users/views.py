from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegisterForm, AvatarForm
from users.models import Avatar
# Create your views here.

class UserRegisterView(CreateView):
    model = User
    template_name = 'users/register.html'
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        response = super().form_valid(form)
        user = authenticate(
            username=form.cleaned_data['username'], password=form.cleaned_data['password1'])
        if user:
            login(self.request, user)
        return response

class UserLoginView(LoginView):
    template_name = 'users/login.html'
    
    def get_success_url(self) -> str:
        return reverse_lazy('platform')

class UserLogoutView(LogoutView):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('login')
    
class ProfileView(DetailView):
    model = User
    template_name = 'users/profile.html'
    
    def get_object(self):
        return self.request.user
    

    
class ProfileUpdateView(UpdateView):
    model = User
    template_name = 'users/profile_update.html'
    fields = ['first_name', 'last_name', 'email']
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user       

class AvatarUpdateView(UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'users/avatar_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        user = self.request.user
        avatar, created = Avatar.objects.get_or_create(user=user)
        return avatar
    