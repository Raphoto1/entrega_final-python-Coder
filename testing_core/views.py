from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from testing_core.forms import TestPlatformForm, TestContextForm, TestForm, AppForm, FakeUserForm, QuestionForm
from testing_core.models import FakeUser, TestPlatform, TestContext, Test, Question, TestQuestion, Answers, App

# Create your views here.
def home(request):
    return render(request, 'testing_core/home.html')

def platform(request):
    testPlatform= TestPlatform.objects.all()
    testContext = TestContext.objects.all()
    testApps = App.objects.all()
    FakeUsers = FakeUser.objects.all()
    Questions = Question.objects.all()
    return render(request, 'testing_core/platform.html', {'testPlatform': testPlatform, 'testContext': testContext, 'apps': testApps, 'FakeUsers': FakeUsers, 'Questions': Questions})


#platform
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
    
#context
class TestContextCreateView(CreateView):
    model = TestContext
    form_class = TestContextForm
    template_name = 'testing_core/testContext/createContext.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class TestContextListView(ListView):
    model = TestContext
    template_name = 'testing_core/testContext/listContext.html'
    context_object_name = 'test_contexts'

class TestContextUpdateView(UpdateView):
    model = TestContext
    form_class = TestContextForm
    template_name = 'testing_core/testContext/updateContext.html'
    success_url = '/listContext/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestContextDeleteView(DeleteView):
    model = TestContext
    template_name = 'testing_core/testContext/deleteContext.html'
    context_object_name = 'test_context'
    success_url = '/listContext/'

class TestContextDetailView(DetailView):
    model = TestContext
    template_name = 'testing_core/testContext/detailContext.html'
    context_object_name = 'test_context'
    
#app
class TestAppCreateView(CreateView):
    model = App
    form_class = AppForm
    template_name = 'testing_core/testApp/createApp.html'
    success_url = '/platform/'

    def form_valid(self, form):
        app = form.save(commit=False)
        app.user = self.request.user  # Asigna el usuario actual
        app.save()
        form.save_m2m()  # Guarda relaciones ManyToMany
        return super().form_valid(form)
    
class TestAppListView(ListView):
    model = App
    template_name = 'testing_core/testApp/listApps.html'
    context_object_name = 'test_apps'
    
class TestAppUpdateView(UpdateView):
    model = App
    form_class = AppForm
    template_name = 'testing_core/testApp/updateApp.html'
    success_url = '/listApps/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestAppDeleteView(DeleteView):
    model = App
    template_name = 'testing_core/testApp/deleteApp.html'
    context_object_name = 'test_app'
    success_url = '/listApps/'

class TestAppDetailView(DetailView):
    model = App
    template_name = 'testing_core/testApp/detailApp.html'
    context_object_name = 'test_app'
    
#fakeUser
class FakeUserCreateView(CreateView):
    model = FakeUser
    form_class = FakeUserForm
    template_name = 'testing_core/fakeUser/createFakeUser.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class FakeUserListView(ListView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/listFakeUser.html'
    context_object_name = 'fake_users'
    
class FakeUserUpdateView(UpdateView):
    model = FakeUser
    form_class = FakeUserForm
    template_name = 'testing_core/fakeUser/updateFakeUser.html'
    success_url = '/listFakeUsers/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class FakeUserDeleteView(DeleteView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/deleteFakeUser.html'
    context_object_name = 'fake_user'
    success_url = '/listFakeUsers/'
    
class FakeUserDetailView(DetailView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/detailFakeUser.html'
    context_object_name = 'fake_user'
    
#question
class QuestionCreateView(CreateView):  
    model = Question
    form_class = QuestionForm
    template_name = 'testing_core/question/createQuestion.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class QuestionListView(ListView):
    model = Question
    template_name = 'testing_core/question/listQuestions.html'
    context_object_name = 'questions'
    
class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'testing_core/question/updateQuestion.html'
    success_url = '/listQuestions/'

    def form_valid(self, form):
        return super().form_valid(form)

class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'testing_core/question/deleteQuestion.html'
    context_object_name = 'question'
    success_url = '/listQuestions/'
    
class QuestionDetailView(DetailView):
    model = Question
    template_name = 'testing_core/question/detailQuestion.html'
    context_object_name = 'question'
    