from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from .models import User, Todo, Attendance
from .forms import UserRegistrationForm, LoginForm, TodoForm

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('index')

@login_required
def todo_list(request):
    if request.method == 'POST':
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.user = request.user
            todo.save()
            return redirect('todo')
    
    todos = Todo.objects.filter(user=request.user)
    form = TodoForm()
    return render(request, 'todo.html', {'todos': todos, 'form': form})

@login_required
def todo_toggle(request, todo_id):
    todo = Todo.objects.get(id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo')

@login_required
def todo_delete(request, todo_id):
    Todo.objects.filter(id=todo_id, user=request.user).delete()
    return redirect('todo')

@login_required
def attendance_check(request):
    today = timezone.now().date()
    already_checked = Attendance.objects.filter(
        user=request.user,
        date=today
    ).exists()
    
    if request.method == 'POST' and not already_checked:
        Attendance.objects.create(user=request.user)
        return redirect('check')
    
    attendances = Attendance.objects.filter(user=request.user)
    return render(request, 'check.html', {
        'already_checked': already_checked,
        'attendances': attendances
    })

@login_required
def teacher_view(request):
    if not request.user.is_teacher:
        return redirect('index')
    
    students = User.objects.filter(is_teacher=False)
    today = timezone.now().date()
    attendance_data = {}
    
    for student in students:
        attendance_data[student] = Attendance.objects.filter(
            user=student,
            date=today
        ).exists()
    
    return render(request, 'teacher.html', {'attendance_data': attendance_data})
