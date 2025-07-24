from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'testing_core/home.html')

def platform(request):
    return render(request, 'testing_core/platform.html')