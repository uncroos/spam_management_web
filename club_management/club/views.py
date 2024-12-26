from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.contrib import messages
from .models import User, Todo, Attendance
from .forms import TeacherRegistrationForm, StudentRegistrationForm, LoginForm, TodoForm
from datetime import timedelta

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        if user_type == 'teacher':
            form = TeacherRegistrationForm(request.POST)
        else:
            form = StudentRegistrationForm(request.POST)
            
        if form.is_valid():
            user = form.save()
            login(request, user)
            if user.is_teacher:
                messages.success(request, f'선생님 계정이 생성되었습니다. 선생님 코드: {user.teacher_code}')
            else:
                messages.success(request, '학생 계정이 생성되었습니다.')
            return redirect('index')
    else:
        user_type = request.GET.get('type', 'student')
        if user_type == 'teacher':
            form = TeacherRegistrationForm()
        else:
            form = StudentRegistrationForm()
    
    return render(request, 'register.html', {
        'form': form,
        'user_type': user_type
    })

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
                messages.error(request, '아이디 또는 비밀번호가 잘못되었습니다.')
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
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('todo')

@login_required
def todo_delete(request, todo_id):
    todo = get_object_or_404(Todo, id=todo_id, user=request.user)
    todo.delete()
    return redirect('todo')

@login_required
def attendance_check(request):
    today = timezone.now().date()
    already_checked = Attendance.objects.filter(
        user=request.user,
        date=today
    ).exists()
    
    if request.method == 'POST' and not already_checked:
        Attendance.objects.create(user=request.user, date=today)
        messages.success(request, '출석체크가 완료되었습니다.')
        return redirect('check')
    
    attendances = Attendance.objects.filter(user=request.user).order_by('-date')
    return render(request, 'check.html', {
        'already_checked': already_checked,
        'attendances': attendances
    })

@login_required
def teacher_view(request):
    if not request.user.is_teacher:
        messages.error(request, '선생님만 접근할 수 있습니다.')
        return redirect('index')
    
    students = User.objects.filter(teacher=request.user, is_teacher=False)
    today = timezone.now().date()
    attendance_data = {}
    
    for student in students:
        attendance_data[student] = {
            'attended': Attendance.objects.filter(user=student, date=today).exists(),
            'total_attendance': Attendance.objects.filter(user=student).count(),
            'todos': Todo.objects.filter(user=student).order_by('-created_at')[:5]  # 최근 5개 Todo
        }
    
    return render(request, 'teacher.html', {
        'attendance_data': attendance_data,
        'teacher_code': request.user.teacher_code,
        'student_count': students.count()
    })

@login_required
def student_detail(request, student_id):
    if not request.user.is_teacher:
        messages.error(request, '선생님만 접근할 수 있습니다.')
        return redirect('index')
    
    student = get_object_or_404(User, id=student_id, teacher=request.user, is_teacher=False)
    
    # 최근 30일 출석 기록 필터링
    recent_30_days = timezone.now().date() - timedelta(days=30)
    attendance_history = Attendance.objects.filter(user=student, date__gte=recent_30_days).order_by('-date')
    todos = Todo.objects.filter(user=student).order_by('-created_at')
    
    # 출석률 계산 (최근 30일 기준)
    total_days = 30
    attended_days = attendance_history.count()
    attendance_rate = (attended_days / total_days) * 100 if total_days > 0 else 0
    
    return render(request, 'student_detail.html', {
        'student': student,
        'attendance_history': attendance_history,
        'todos': todos,
        'attendance_rate': attendance_rate
    })