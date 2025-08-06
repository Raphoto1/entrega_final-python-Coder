from django.contrib import messages
from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView, FormView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from testing_core.forms import TestPlatformForm, TestContextForm, TestForm, AppForm, FakeUserForm, QuestionForm, TestQuestionForm, TestCommitForm
from testing_core.models import FakeUser, TestPlatform, TestContext, Test, Question, TestQuestion, Answers, App, TestCommit, TestResult, TestQuestion, Question, Answers


# Create your views here.
def home(request):
    return render(request, 'testing_core/home.html')

def about(request):
    return render(request, 'testing_core/about.html')

@login_required
def platform(request):
    testPlatform= TestPlatform.objects.all()
    testContext = TestContext.objects.all()
    testApps = App.objects.all()
    FakeUsers = FakeUser.objects.all()
    Questions = Question.objects.all()
    tests = Test.objects.all()
    testCommits = TestCommit.objects.all()
    return render(request, 'testing_core/platform.html', {'testPlatform': testPlatform, 'testContext': testContext, 'apps': testApps, 'FakeUsers': FakeUsers, 'Questions': Questions, 'tests' : tests, 'testCommits': testCommits})


#platform
class TestPlatformCreateView(LoginRequiredMixin, CreateView):
    model = TestPlatform
    form_class = TestPlatformForm
    template_name = 'testing_core/testPlatform/createPlatform.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class TestPlatformListView(LoginRequiredMixin, ListView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/listPlatforms.html'
    context_object_name = 'test_platforms'
    
class TestPlatformUpdateView(LoginRequiredMixin, UpdateView):
    model = TestPlatform
    form_class = TestPlatformForm
    template_name = 'testing_core/testPlatform/updatePlatform.html'
    success_url = '/listPlatforms/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestPlatformDeleteView(LoginRequiredMixin, DeleteView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/deletePlatform.html'
    context_object_name = 'test_platform'
    success_url = '/listPlatforms/'

class TestPlatformDetailView(LoginRequiredMixin, DetailView):
    model = TestPlatform
    template_name = 'testing_core/testPlatform/detailPlatform.html'
    context_object_name = 'test_platform'
    
#context
class TestContextCreateView(LoginRequiredMixin, CreateView):
    model = TestContext
    form_class = TestContextForm
    template_name = 'testing_core/testContext/createContext.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class TestContextListView(LoginRequiredMixin, ListView):
    model = TestContext
    template_name = 'testing_core/testContext/listContext.html'
    context_object_name = 'test_contexts'

class TestContextUpdateView(LoginRequiredMixin, UpdateView):
    model = TestContext
    form_class = TestContextForm
    template_name = 'testing_core/testContext/updateContext.html'
    success_url = '/listContext/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestContextDeleteView(LoginRequiredMixin, DeleteView):
    model = TestContext
    template_name = 'testing_core/testContext/deleteContext.html'
    context_object_name = 'test_context'
    success_url = '/listContext/'

class TestContextDetailView(LoginRequiredMixin, DetailView):
    model = TestContext
    template_name = 'testing_core/testContext/detailContext.html'
    context_object_name = 'test_context'
    
#app
class TestAppCreateView(LoginRequiredMixin, CreateView):
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
    
class TestAppListView(LoginRequiredMixin, ListView):
    model = App
    template_name = 'testing_core/testApp/listApps.html'
    context_object_name = 'test_apps'
    
class TestAppUpdateView(LoginRequiredMixin, UpdateView):
    model = App
    form_class = AppForm
    template_name = 'testing_core/testApp/updateApp.html'
    success_url = '/listApps/'

    def form_valid(self, form):
        return super().form_valid(form)

class TestAppDeleteView(LoginRequiredMixin, DeleteView):
    model = App
    template_name = 'testing_core/testApp/deleteApp.html'
    context_object_name = 'test_app'
    success_url = '/listApps/'

class TestAppDetailView(LoginRequiredMixin, DetailView):
    model = App
    template_name = 'testing_core/testApp/detailApp.html'
    context_object_name = 'test_app'
    
#fakeUser
class FakeUserCreateView(LoginRequiredMixin, CreateView):
    model = FakeUser
    form_class = FakeUserForm
    template_name = 'testing_core/fakeUser/createFakeUser.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class FakeUserListView(LoginRequiredMixin, ListView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/listFakeUser.html'
    context_object_name = 'fake_users'
    
class FakeUserUpdateView(LoginRequiredMixin, UpdateView):
    model = FakeUser
    form_class = FakeUserForm
    template_name = 'testing_core/fakeUser/updateFakeUser.html'
    success_url = '/listFakeUsers/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class FakeUserDeleteView(LoginRequiredMixin, DeleteView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/deleteFakeUser.html'
    context_object_name = 'fake_user'
    success_url = '/listFakeUsers/'
    
class FakeUserDetailView(LoginRequiredMixin, DetailView):
    model = FakeUser
    template_name = 'testing_core/fakeUser/detailFakeUser.html'
    context_object_name = 'fake_user'
    
#question
class QuestionCreateView(LoginRequiredMixin, CreateView):  
    model = Question
    form_class = QuestionForm
    template_name = 'testing_core/question/createQuestion.html'
    success_url = '/platform/'

    def form_valid(self, form):
        return super().form_valid(form)
    
class QuestionListView(LoginRequiredMixin, ListView):
    model = Question
    template_name = 'testing_core/question/listQuestions.html'
    context_object_name = 'questions'
    
class QuestionUpdateView(LoginRequiredMixin, UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = 'testing_core/question/updateQuestion.html'
    success_url = '/listQuestions/'

    def form_valid(self, form):
        return super().form_valid(form)

class QuestionDeleteView(LoginRequiredMixin, DeleteView):
    model = Question
    template_name = 'testing_core/question/deleteQuestion.html'
    context_object_name = 'question'
    success_url = '/listQuestions/'
    
class QuestionDetailView(LoginRequiredMixin, DetailView):
    model = Question
    template_name = 'testing_core/question/detailQuestion.html'
    context_object_name = 'question'

#tests
class TestCreateView(LoginRequiredMixin, CreateView):
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
    
class TestListView(LoginRequiredMixin, ListView):
    model = Test
    template_name = 'testing_core/testTemp/listTests.html'
    context_object_name = 'tests'
    
class TestUpdateView(LoginRequiredMixin, UpdateView):
    model = Test
    form_class = TestForm
    template_name = 'testing_core/testTemp/updateTest.html'
    success_url = '/listTests/'

    def form_valid(self, form):
        return super().form_valid(form)   
    
class TestDeleteView(LoginRequiredMixin, DeleteView):
    model = Test
    template_name = 'testing_core/testTemp/deleteTest.html'
    context_object_name = 'test'
    success_url = '/listTests/'
    
class TestDetailView(LoginRequiredMixin, DetailView):
    model = Test
    template_name = 'testing_core/testTemp/detailTest.html'
    context_object_name = 'test'
        
class DeleteQuestionforTestView(LoginRequiredMixin, DeleteView):
    model = TestQuestion
    template_name = 'testing_core/testQuestions/deleteTestQuestions.html'

    def get_success_url(self):
        return reverse_lazy('detail_test', kwargs={'pk': self.object.test.pk})
  
class CreateQuestionsForTests(LoginRequiredMixin, FormView):
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

class UpdateQuestionsForTest(LoginRequiredMixin, FormView):
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

# Función para duplicar un Test
@login_required
def duplicate_test(request, pk):
    original = get_object_or_404(Test, pk=pk)

    # Duplicamos el objeto Test
    copy = Test.objects.create(
        app=original.app,
        name=f"{original.name} (copia)",
        description=original.description,
        creator_user=original.creator_user,
        test_context=original.test_context,
        test_platform=original.test_platform,
        # Podés setear otras propiedades si es necesario
    )

    # Duplicamos preguntas si son relaciones M2M
    for tq in original.questions.all():  # gracias al related_name='questions'
        TestQuestion.objects.create(
            test=copy,
            questions=tq.questions,  # copiamos la misma pregunta
        )

    messages.success(request, f"Test duplicado con sus preguntas: {copy.name}")
    return redirect("list_tests")

#testCommit desarrollo futuro

class CreateTestCommitView(LoginRequiredMixin, CreateView):
    model = TestCommit
    form_class = TestCommitForm
    template_name = 'testing_core/testCommit/createTestCommit.html'
    success_url = reverse_lazy('list_test_commit')

    def form_valid(self, form):
        form.instance.status = 'pending'
        return super().form_valid(form)

class ListTestCommitView(LoginRequiredMixin, ListView):
    model = TestCommit
    template_name = 'testing_core/testCommit/listTestCommits.html'
    context_object_name = 'testCommits'

#make Test

class CreateMakeTest(LoginRequiredMixin, CreateView):
    model = Test
    template_name = 'testing_core/testTemp/createTest.html'
    success_url = '/listTests/'

    def get(self, request, *args, **kwargs):
        test = Test()
        questions = Question.objects.all()
        return self.render_to_response({'test': test, 'questions': questions})

    def post(self, request, *args, **kwargs):
        # Recuperamos los datos del formulario
        test_name = request.POST.get('name')
        test_description = request.POST.get('description')

        test_platform_id = request.POST.get('testPlatform')
        test_context_id = request.POST.get('testContext')

        questions_ids = request.POST.getlist('questions')

        # Creamos el nuevo Test
        new_test = Test()
        new_test.name = test_name
        new_test.description = test_description

        # Asignamos la plataforma y contexto
        test_platform = get_object_or_404(TestPlatform, pk=test_platform_id)
        test_context = get_object_or_404(TestContext, pk=test_context_id)
        new_test.test_platform = test_platform
        new_test.test_context = test_context

        # Creamos las preguntas relacionadas con el Test
        for question_id in questions_ids:
            question = get_object_or_404(Question, pk=question_id)
            new_test.questions.add(question)

        # Guardamos el nuevo Test en la base de datos
        new_test.save()

        return self.get_success_response(new_test.pk)

    def get_success_response(self, test_pk):
        messages.success(self.request, f'Test creado correctamente: {test_pk}')
        return redirect('detail_test', pk=test_pk)

@login_required  
def detail_make_test(request, pk):
    test = get_object_or_404(Test, pk=pk)
    test_questions = TestQuestion.objects.filter(test=test).select_related('questions')

    answers_by_question = []

    for tq in test_questions:
        question = tq.questions
        try:
            answer_obj = Answers.objects.get(test=test, question=question)
            answer_text = answer_obj.answer_text
        except Answers.DoesNotExist:
            answer_text = None

        answers_by_question.append({
            'question': question,
            'answer': answer_text
        })
    context = {
        'test': test,
        'test_questions': test_questions,
        'answers_by_question': answers_by_question,
    }

    return render(request, 'testing_core/makeTest/detailMakeTest.html', context)

@login_required
def save_answer(request, pk, question_id):
    test = get_object_or_404(Test, pk=pk)
    question = get_object_or_404(Question, pk=question_id)
    answer_text = request.POST.get('answer')

    obj, created = Answers.objects.update_or_create(
        test=test,
        question=question,
        defaults={'answer_text': answer_text}
    )

    if created:
        messages.success(request, "Respuesta registrada correctamente.")
    else:
        messages.info(request, "Respuesta actualizada para esta pregunta.")

    return redirect('detail_make_test', pk=test.pk)


    