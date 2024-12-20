from django.contrib import admin
from django.urls import path
from main import views  # main 앱의 뷰를 가져옵니다.

urlpatterns = [
    path('admin/', admin.site.urls),  # 관리자 페이지
    path('', views.home, name='home'),  # 루트 경로를 home 뷰에 연결
]