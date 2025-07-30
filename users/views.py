from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, update_session_auth_hash
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import PasswordChangeForm

from users.forms import RegisterForm, AvatarForm, ProfileUpdateForm, ProfileRoleForm
from users.models import Avatar, Role
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

class UserLogoutView(LoginRequiredMixin, View):
    template_name = 'users/logout.html'
    next_page = reverse_lazy('login')
    
class ProfileView(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'users/profile.html'
    
    def get_object(self):
        return self.request.user
    
class AvatarUpdateView(LoginRequiredMixin, UpdateView):
    model = Avatar
    form_class = AvatarForm
    template_name = 'users/avatar_update.html'
    success_url = reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        user = self.request.user
        avatar, created = Avatar.objects.get_or_create(user=user)
        return avatar

class ProfileRoleView(LoginRequiredMixin, View):
    template_name = "users/profile_role.html"
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        role, created = Role.objects.get_or_create(user=request.user)
        role_form = ProfileRoleForm(instance=role)
        context = {"role_form": role_form}
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        role, created = Role.objects.get_or_create(user=request.user)
        role_form = ProfileRoleForm(request.POST, instance=role)
        if role_form.is_valid():
            role_form.save()
            return redirect('profile')
        context = {"role_form": role_form}
        return render(request, self.template_name, context)
    
class ProfileUpdateView(LoginRequiredMixin, View):
    template_name = "users/profile_update.html"
    success_url = reverse_lazy("profile")

    def get(self, request, *args, **kwargs):
        user_form = ProfileUpdateForm(instance=request.user)
        # Obtenemos o creamos el avatar del usuario
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(instance=avatar)
        password_form = PasswordChangeForm(request.user)
        context = {
            "user_form": user_form,
            "avatar_form": avatar_form,
            "password_form": password_form,
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        # Inicializamos formularios con la data enviada.
        user_form = ProfileUpdateForm(request.POST, instance=request.user)
        avatar, _ = Avatar.objects.get_or_create(user=request.user)
        avatar_form = AvatarForm(request.POST, request.FILES, instance=avatar)
        password_form = PasswordChangeForm(request.user, request.POST)

        if "profile_update" in request.POST:
            # Se envió el formulario para actualizar datos y avatar.
            if user_form.is_valid() and avatar_form.is_valid():
                user_form.save()
                avatar_form.save()
                return redirect('profile')
        elif "change_password" in request.POST:
            # Se envió el formulario para cambiar contraseña.
            if password_form.is_valid():
                user = password_form.save()
                # Importante: actualizar la sesión para que el usuario no se desconecte.
                update_session_auth_hash(request, user)
                return redirect('profile')

        context = {
            "user_form": user_form,
            "avatar_form": avatar_form,
            "password_form": password_form,
        }
        return render(request, self.template_name, context) 

    