from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
from .models import Avatar, Role


class RegisterForm(UserCreationForm):
    usable_password = None

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', ]
        labels = {'username': 'Nombre de Usuario',
                  'email': 'Email',
                  'password1': 'Password',
                  'password2': 'Confirmar Password'}
        
class AvatarForm(forms.ModelForm):
    class Meta:
        model = Avatar
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].label = "Avatar Image"
        
class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["username", "email", "first_name", "last_name"]
        

class ProfileRoleForm(forms.ModelForm):
    ROLE_CHOICES = [
        ('tester', 'Tester'),
        ('dev', 'Developer'),
        ('manager', 'Manager'),
        ('viewer', 'Viewer')
    ]
    name = forms.ChoiceField(choices=ROLE_CHOICES, label="Que Rol Asignar", widget=forms.Select(attrs={'class': 'form-control'}))

    class Meta:
        model = Role
        fields = ['name', 'description']
        widgets = {
            'description': forms.Textarea(attrs={'class': 'form-control'}),
        }
        labels = {
            'description': "Role Description"
        }

