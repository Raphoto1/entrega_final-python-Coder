from django import forms
from .models import App, Question, TestContext, TestPlatform, FakeUser

class TestPlatformForm(forms.ModelForm):
    class Meta:
        model = TestPlatform
        fields = ['name', 'version']
        
class TestContextForm(forms.ModelForm):
    class Meta:
        model = TestContext
        fields = [
            'name', 'test_platform', 'mobile', 'mobile_carrier',
            'mobile_number', 'mobile_contract', 'signal_strength',
            'connection_speed', 'web', 'web_browser', 'description'
        ]
        
class AppForm(forms.ModelForm):
    test_platforms = forms.ModelMultipleChoiceField(
        queryset=TestPlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Plataformas'
    )

    class Meta:
        model = App
        fields = ['name', 'current_version', 'description', 'test_platforms']
        labels = {
            'name': 'Nombre',
            'current_version': 'Versión Actual',
            'description': 'Descripción',
        }

class FakeUserForm(forms.ModelForm):
    class Meta:
        model = FakeUser
        fields = ['name', 'last_name', 'fake_username', 'email', 'password', 'phone_number', 'age']
        widgets = {
            'password': forms.PasswordInput(),
        }
        labels = {
            'name': 'Nombre',
            'last_name': 'Apellido',
            'fake_username': 'Nombre de Usuario Falso',
            'email': 'Correo Electrónico',
            'password': 'Contraseña',
            'phone_number': 'Número de Teléfono',
            'age': 'Edad',
        }

class TestForm(forms.Form):
    name = forms.CharField(label='Test Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    app = forms.ModelChoiceField(
        queryset=App.objects.all(),
        label='App'
    )
    fakeUser = forms.ModelChoiceField(
        queryset=FakeUser.objects.all(),
        label='Fake User'
    )
    test_platform = forms.ModelChoiceField(
        queryset=TestPlatform.objects.all(),
        label='Platform'
    )   
    test_context = forms.ModelChoiceField(
        queryset=TestContext.objects.all(),
        label='Context'
    )
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Questions'
    )
    

    
class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question Text', max_length=255)
    spected_answer = forms.CharField(label='Spected Answer', widget=forms.Textarea)
    reference_image = forms.ImageField(label='Reference Image', required=False)
    
   