# main/urls.py (앱의 urls.py)
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),  # 이 부분을 수정
    path('', views.home, name='home'),      # 이 부분을 추가
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('todo/', views.todo_view, name='todo'),
    path('attendance/', views.attendance_view, name='attendance'),
]