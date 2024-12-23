from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo, Attendance

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'phone_number', 'is_teacher')
    fieldsets = UserAdmin.fieldsets + (
        ('추가 정보', {'fields': ('phone_number', 'is_teacher')}),
    )

class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_completed', 'created_at')
    list_filter = ('user', 'is_completed')

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date')
    list_filter = ('user', 'date')

admin.site.register(User, CustomUserAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Attendance, AttendanceAdmin)