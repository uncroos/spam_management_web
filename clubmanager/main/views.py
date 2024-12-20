from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'main/home.html')

@login_required
def attendance(request):
    if request.method == 'POST':
        # 출석 처리 로직
        pass
    return render(request, 'main/attendance.html')

@login_required
def todo_list(request):
    if request.method == 'POST':
        # To-do 추가/완료 처리 로직
        pass
    return render(request, 'main/todo_list.html')