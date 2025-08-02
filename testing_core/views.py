from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.decorators import login_required

from testing_core.forms import TestPlatformForm, TestContextForm, TestForm, AppForm, FakeUserForm, QuestionForm, TestQuestionForm
from testing_core.models import FakeUser, TestPlatform, TestContext, Test, Question, TestQuestion, Answers, App


# Create your views here.
def home(request):
    return render(request, 'testing_core/home.html')

@login_required
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

#tests
class TestCreateView(CreateView):
    model = Test
    form_class = TestForm
    template_name = 'testing_core/testTemp/createTest.html'
    success_url = '/createcreate_questions_to_test/'

    def get_success_url(self):
        return reverse('create_questions_to_test', args=[self.object.pk])

    def form_valid(self, form):
        test = form.save(commit=False)
        test.creator_user = self.request.user
        test.save()
        form.save_m2m()  # Guarda relaciones ManyToMany
        return super().form_valid(form)
    
class TestListView(ListView):
    model = Test
    template_name = 'testing_core/testTemp/listTests.html'
    context_object_name = 'tests'
    
class TestUpdateView(UpdateView):
    model = Test
    form_class = TestForm
    template_name = 'testing_core/testTemp/updateTest.html'
    success_url = '/listTests/'

    def form_valid(self, form):
        return super().form_valid(form)   
    
class TestDeleteView(DeleteView):
    model = Test
    template_name = 'testing_core/testTemp/deleteTest.html'
    context_object_name = 'test'
    success_url = '/listTests/'
    
class TestDetailView(DetailView):
    model = Test
    template_name = 'testing_core/testTemp/detailTest.html'
    context_object_name = 'test'
        
class DeleteQuestionforTestView(DeleteView):
    model = TestQuestion
    template_name = 'testing_core/testQuestions/deleteTestQuestions.html'

    def get_success_url(self):
        return reverse_lazy('detail_test', kwargs={'pk': self.object.test.pk})

    
class CreateQuestionsForTests(FormView):
    form_class = TestQuestionForm
    template_name = 'testing_core/testQuestions/createTestQuestions.html' 

    def get_test(self):
        return get_object_or_404(Test, pk=self.kwargs.get('test_id'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['test'] = self.get_test() 
        return kwargs

    def form_valid(self, form):
        test = self.get_test()
        questions = form.cleaned_data.get('questions')

        if not questions:
            form.add_error('questions', 'Debes seleccionar al menos una pregunta.')
            return self.form_invalid(form)

        for question in questions:
            exists = TestQuestion.objects.filter(test=test, questions=question).exists()
            if not exists:
                TestQuestion.objects.create(test=test, questions=question)

        return redirect('detail_test', pk=test.pk)

    def form_invalid(self, form):
        print("DEBUG Vista — formulario inválido")
        print("DEBUG Vista — errores:", form.errors)
        return super().form_invalid(form)

class UpdateQuestionsForTest(FormView):
    form_class = TestQuestionForm
    template_name = 'testing_core/testQuestions/updateTestQuestions.html'

    def get_test(self):
        return get_object_or_404(Test, pk=self.kwargs.get('test_id'))

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['test'] = self.get_test()
        return kwargs

    def form_valid(self, form):
        test = self.get_test()
        selected_questions = form.cleaned_data.get('questions')

        # 🔥 Eliminamos vínculos previos
        TestQuestion.objects.filter(test=test).delete()

        # ✅ Creamos nuevas relaciones evitando duplicados
        for question in selected_questions:
            TestQuestion.objects.create(test=test, questions=question)

        return redirect('detail_test', pk=test.pk)

    def form_invalid(self, form):
        print("DEBUG UpdateView — formulario inválido")
        print("DEBUG UpdateView — errores:", form.errors)
        return super().form_invalid(form)

