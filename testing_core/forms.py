from django import forms
from .models import App, Question, TestContext, TestPlatform, FakeUser, Test, TestQuestion

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

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'spected_answer', 'reference_image']
        widgets = {
            'spected_answer': forms.Textarea(),
            'reference_image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }
        
class TestForm(forms.ModelForm):
    class Meta:
        model = Test
        fields = ['name', 'app', 'test_context', 'test_platform','fakeUser', 'description']
        labels = {
            'name': 'Nombre del Test',
            'app': 'Aplicación',
            'test_context': 'Contexto de Test',
            'test_platform': 'Plataforma de Test',
            'fakeUser': 'Usuario Falso',
            'description': 'Descripción',
        }  
   

class TestQuestionForm(forms.Form):
    questions = forms.ModelMultipleChoiceField(
        queryset=Question.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
        label="Selecciona las preguntas para este test"
    )

    def __init__(self, *args, **kwargs):
        self.test = kwargs.pop('test', None)
        super().__init__(*args, **kwargs)

        # Preseleccionar preguntas asociadas al test
        if self.test:
            initial_qs = Question.objects.filter(tests__test=self.test)
            self.initial['questions'] = initial_qs

    def clean_questions(self):
        data = self.cleaned_data.get('questions')
        if not data:
            raise forms.ValidationError("Debes seleccionar al menos una pregunta.")
        return data



