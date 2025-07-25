from django.db import models
from django.utils import timezone

# Create your models here.
# form check
class TestPlatform(models.Model):
    name = models.CharField(max_length=100)
    version = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
# form check
class TestContext(models.Model):
    name = models.CharField(max_length=100)
    test_platform = models.ForeignKey(TestPlatform, related_name='contexts', on_delete=models.CASCADE)
    mobile = models.BooleanField(default=False)
    mobile_carrier = models.CharField(max_length=100, blank=True, null=True)
    mobile_number = models.CharField(max_length=15, blank=True, null=True)
    mobile_contract = models.CharField(max_length=100, blank=True, null=True)
    signal_strength = models.IntegerField(blank=True, null=True)
    connection_speed = models.CharField(max_length=100, blank=True, null=True)
    web = models.BooleanField(default=False)
    web_browser = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

# form check    
class App(models.Model):
    user = models.ForeignKey('auth.User', related_name='apps', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, unique=True)
    test_platforms = models.ManyToManyField(TestPlatform, related_name='apps')
    versions = models.CharField(max_length=50)
    current_version = models.CharField(max_length=50)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FakeUser(models.Model):
    name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, blank=True, null=True)
    fake_username = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    
class Test(models.Model):
    creator_user = models.ForeignKey('auth.User', related_name='tests', on_delete=models.CASCADE)
    fakeUser = models.ForeignKey('fakeUser', related_name='tests', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    app = models.ForeignKey('app', related_name='tests', on_delete=models.CASCADE)
    test_context = models.ForeignKey(TestContext, related_name='tests', on_delete=models.CASCADE)
    test_platform = models.ForeignKey(TestPlatform, related_name='tests', on_delete=models.CASCADE)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
  
class Question(models.Model):
    question_text = models.CharField(max_length=255)
    spected_answer = models.TextField()
    reference_image = models.ImageField(upload_to='questions/', null=True, blank=True)

    def __str__(self):
        return self.question_text
 #form NOT NEEDED   
class TestQuestion(models.Model):
    test = models.ForeignKey(Test, related_name='questions', on_delete=models.CASCADE)
    questions = models.ForeignKey(Question, related_name='tests', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.test.name} - {self.questions.question_text}"

class Answers(models.Model):
    test = models.ForeignKey(Test, related_name='answers', on_delete=models.CASCADE)
    question = models.ForeignKey(Question, related_name='answers', on_delete=models.CASCADE)
    answer_text = models.TextField()
    answer_image = models.ImageField(upload_to='answers/', null=True, blank=True)

    def __str__(self):
        return f"{self.test.name} - {self.question.question_text}: {self.answer_text}"
    

    
class TestResult(models.Model):
    user = models.ForeignKey('auth.User', related_name='test_results', on_delete=models.CASCADE)
    test = models.ForeignKey(Test, related_name='results', on_delete=models.CASCADE)
    notes = models.TextField(blank=True, null=True)
    started_at = models.DateTimeField(auto_now_add=True)
    finished_at = models.DateTimeField(auto_now=True)
    score = models.FloatField()
    passed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test.name} - {'Passed' if self.passed else 'Failed'}"

class AnswerFeedback(models.Model):
    answer = models.ForeignKey(Answers, related_name='feedbacks', on_delete=models.CASCADE)
    reviewer = models.ForeignKey('auth.User', related_name='answer_feedbacks', on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    score = models.FloatField(blank=True, null=True)  # Opcional, si quieres puntuar la respuesta

    def __str__(self):
        return f"Feedback by {self.reviewer} on {self.answer}"
    
class TestStatus(models.Model):
    test_status_id = models.AutoField(primary_key=True)
    test = models.ForeignKey(Test, related_name='statuses', on_delete=models.CASCADE, null=True, blank=True)
    app = models.ForeignKey(App, related_name='statuses', on_delete=models.CASCADE, default=None, null=True, blank=True)
    user = models.ForeignKey('auth.User', related_name='test_statuses', on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(max_length=50)  # Ejemplo: 'pending', 'in_progress', 'completed'
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.test_status_id} - {self.status}"

