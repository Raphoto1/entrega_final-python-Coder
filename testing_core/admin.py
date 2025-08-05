from django.contrib import admin

# Register your models here.
from .models import TestPlatform, TestContext, Test, Question, TestQuestion, Answers, TestResult, AnswerFeedback, FakeUser, App, TestCommit

register_models = [
    TestPlatform,
    TestContext,
    Test,
    Question,
    TestQuestion,
    Answers,
    TestResult,
    AnswerFeedback,
    FakeUser,
    App,
    TestCommit
]

admin.site.register(register_models)