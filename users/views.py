from django.shortcuts import render
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.views import LoginView, LogoutView

from users.forms import RegisterForm
# Create your views here.

def test_view(request):
    return render(request, 'users/test.html')

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
