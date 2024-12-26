from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import random
import string

class User(AbstractUser):
    phone_number = models.CharField(max_length=15)
    is_teacher = models.BooleanField(default=False)
    teacher_code = models.CharField(max_length=6, unique=True, null=True, blank=True)
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='students')
    
    def save(self, *args, **kwargs):
        if self.is_teacher and not self.teacher_code:
            # 선생님 계정 생성 시 6자리 고유 코드 생성
            while True:
                code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
                if not User.objects.filter(teacher_code=code).exists():
                    self.teacher_code = code
                    break
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.username

class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    is_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username}'s todo: {self.content}"

class Attendance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    
    class Meta:
        unique_together = ['user', 'date']
    
    def __str__(self):
        return f"{self.user.username}'s attendance on {self.date}"