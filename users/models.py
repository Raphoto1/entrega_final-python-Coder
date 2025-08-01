from django.db import models

# Create your models here.

class Avatar(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='avatar')
    image = models.ImageField(upload_to='avatars/', default='avatars/default.png')

    def __str__(self):
        return f"{self.user.username}'s Avatar"
    
class Role(models.Model):
    user = models.OneToOneField('auth.User', on_delete=models.CASCADE, related_name='role')
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
