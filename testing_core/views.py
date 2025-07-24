from django.shortcuts import redirect, render

from testing_core.forms import TestPlatformForm
from testing_core.models import TestPlatform

# Create your views here.
def home(request):
    return render(request, 'testing_core/home.html')

def platform(request):
    return render(request, 'testing_core/platform.html')

def create_platform(request):
    if request.method == 'POST':
        form = TestPlatformForm(request.POST)
        if form.is_valid():
            platform = TestPlatform(
                name=form.cleaned_data['name'],
                version=form.cleaned_data['version']
            )
            platform.save()
            return redirect('platform')
    else:
        form = TestPlatformForm()
    return render(request, 'testing_core/createPlatform.html', {'form': form})