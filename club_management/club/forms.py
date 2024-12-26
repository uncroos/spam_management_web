from django import forms
from .models import User, Todo

class TeacherRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'phone_number']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

class StudentRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    teacher_code = forms.CharField(max_length=6, required=True)
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'phone_number']
    
    def clean_teacher_code(self):
        code = self.cleaned_data.get('teacher_code')
        try:
            teacher = User.objects.get(teacher_code=code, is_teacher=True)
            return code
        except User.DoesNotExist:
            raise forms.ValidationError("유효하지 않은 선생님 코드입니다.")
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = False
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
            # 선생님 연결
            teacher = User.objects.get(teacher_code=self.cleaned_data['teacher_code'])
            user.teacher = teacher
            user.save()
        return user

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']