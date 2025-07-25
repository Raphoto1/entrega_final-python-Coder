from django import forms
from .models import App, Question, TestContext, TestPlatform, FakeUser

class TestPlatformForm(forms.ModelForm):
    class Meta:
        model = TestPlatform
        fields = ['name', 'version']

class TestContextForm(forms.Form):
    name = forms.CharField(label='Context Name', max_length=100)
    test_platform = forms.ModelChoiceField(
        queryset=TestPlatform.objects.all(),
        label='Test Platform'
    )
    mobile = forms.BooleanField(label='Is Mobile?', required=False)
    mobile_carrier = forms.CharField(label='Mobile Carrier', max_length=100, required=False)
    mobile_number = forms.CharField(label='Mobile Number', max_length=15, required=False)
    mobile_contract = forms.CharField(label='Mobile Contract', max_length=100, required=False)
    signal_strength = forms.CharField(label='Signal Strength', max_length=100, required=False)
    connection_speed = forms.CharField(label='Connection Speed', max_length=100, required=False)
    web = forms.BooleanField(label='Is Web?', required=False)
    web_browser = forms.CharField(label='Web Browser', max_length=100, required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)    

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
    
class AppForm(forms.Form):
    name = forms.CharField(label='App Name', max_length=100)
    current_version = forms.CharField(label='Current Version', max_length=50, required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    platforms = forms.ModelMultipleChoiceField(
        queryset=TestPlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Platforms'
    )
    
class QuestionForm(forms.Form):
    question_text = forms.CharField(label='Question Text', max_length=255)
    spected_answer = forms.CharField(label='Spected Answer', widget=forms.Textarea)
    reference_image = forms.ImageField(label='Reference Image', required=False)
    
class FakeUserForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    last_name = forms.CharField(label='Last Name', max_length=100, required=False)
    fake_username = forms.CharField(label='Fake Username', max_length=100, required=False)
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    phone_number = forms.CharField(label='Phone Number', max_length=15, required=False)
    age = forms.IntegerField(label='Age', required=False)