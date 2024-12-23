from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('todo/', views.todo_list, name='todo'),
    path('todo/toggle/<int:todo_id>/', views.todo_toggle, name='todo_toggle'),
    path('todo/delete/<int:todo_id>/', views.todo_delete, name='todo_delete'),
    path('attendance/', views.attendance_check, name='check'),
    path('teacher/', views.teacher_view, name='teacher'),
]