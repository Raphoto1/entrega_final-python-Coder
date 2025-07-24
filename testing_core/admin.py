from django.contrib import admin

# Register your models here.
from .models import TestPlatform, TestContext, Test, Question, TestQuestion, Answers, TestResult, AnswerFeedback, TestStatus, FakeUser, App

register_models = [
    TestPlatform,
    TestContext,
    Test,
    Question,
    TestQuestion,
    Answers,
    TestResult,
    AnswerFeedback,
    TestStatus,
    FakeUser,
    App,
]

admin.site.register(register_models)