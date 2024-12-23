# views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Todo, Attendance
from datetime import date

def home(request):
    return render(request, 'main/home.html')

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# todo와 attendance는 로그인이 필요한 기능이므로 @login_required 유지
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def todo_view(request):
    if request.method == 'POST':
        if 'add' in request.POST:
            title = request.POST.get('title')
            Todo.objects.create(user=request.user, title=title)
        elif 'toggle' in request.POST:
            todo_id = request.POST.get('todo_id')
            todo = Todo.objects.get(id=todo_id)
            todo.completed = not todo.completed
            todo.save()
    
    todos = Todo.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'main/todo.html', {'todos': todos})

@login_required(login_url='login')
def attendance_view(request):
    today = date.today()
    if request.method == 'POST':
        Attendance.objects.create(user=request.user, date=today)
        return redirect('attendance')
    
    attendance = Attendance.objects.filter(user=request.user).order_by('-date')
    today_attendance = attendance.filter(date=today).exists()
    
    return render(request, 'main/attendance.html', {
        'attendance': attendance,
        'today_attendance': today_attendance
    })