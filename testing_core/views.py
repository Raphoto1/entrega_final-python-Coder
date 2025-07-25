from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from testing_core.forms import TestPlatformForm, TestContextForm, TestForm, AppForm
from testing_core.models import TestPlatform, TestContext, Test, Question, TestQuestion, Answers

# Create your views here.
def home(request):

    return render(request, 'testing_core/home.html')

def platform(request):
    testPlatform= TestPlatform.objects.all()
    testContext = TestContext.objects.all()
    return render(request, 'testing_core/platform.html', {'testPlatform': testPlatform, 'testContext': testContext  })

def create_context(request):
    if request.method == 'POST':
        form = TestContextForm(request.POST)
        if form.is_valid():
            context = TestContext(
                name=form.cleaned_data['name'],
                test_platform=form.cleaned_data['test_platform'],
                mobile=form.cleaned_data['mobile'],
                mobile_carrier=form.cleaned_data['mobile_carrier'],
                mobile_number=form.cleaned_data['mobile_number'],
                mobile_contract=form.cleaned_data['mobile_contract'],
                signal_strength=form.cleaned_data['signal_strength'],
                connection_speed=form.cleaned_data['connection_speed'],
                web=form.cleaned_data['web'],
                web_browser=form.cleaned_data['web_browser'],
                description=form.cleaned_data['description']
            )
            context.save()
            return redirect('platform')
    else:
        form = TestContextForm()
    return render(request, 'testing_core/createContext.html', {'form': form})

class TestPlatformCreateView(CreateView):
    model = TestPlatform
    form_class = TestPlatformForm
    template_name = 'testing_core/testPlatform/createPlatform.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class TestPlatformListView(ListView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/listPlatforms.html'
    context_object_name = 'test_platforms'
    
class TestPlatformUpdateView(UpdateView):
    model = TestPlatform
    form_class = TestPlatformForm
    template_name = 'testing_core/testPlatform/updatePlatform.html'
    success_url = '/listPlatforms/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestPlatformDeleteView(DeleteView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/deletePlatform.html'
    context_object_name = 'test_platform'
    success_url = '/listPlatforms/'

class TestPlatformDetailView(DetailView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/detailPlatform.html'
    context_object_name = 'test_platform'