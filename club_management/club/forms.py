from django import forms
from .models import User, Todo

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'phone_number', 'is_teacher']

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())

class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['content']