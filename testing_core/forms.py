from django import forms
from .models import TestPlatform

class TestPlatformForm(forms.Form):
    name = forms.CharField(label='Platform Name', max_length=100)
    version = forms.CharField(label='Version', widget=forms.Textarea, required=False)

class TestForm(forms.Form):
    name = forms.CharField(label='Test Name', max_length=100)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    platform = forms.ChoiceField(label='Platform', choices=[('web', 'Web'), ('mobile', 'Mobile')])
    context = forms.CharField(label='Context', max_length=200, required=False)
    questions = forms.CharField(label='Questions', widget=forms.Textarea, required=False)
    
class AppForm(forms.Form):
    name = forms.CharField(label='App Name', max_length=100)
    current_version = forms.CharField(label='Current Version', max_length=50, required=False)
    description = forms.CharField(label='Description', widget=forms.Textarea, required=False)
    platforms = forms.ModelMultipleChoiceField(
        queryset=TestPlatform.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        label='Platforms'
    )