from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Todo, Attendance

class CustomUserAdmin(UserAdmin):
    list_display = ('username', 'first_name', 'phone_number', 'is_teacher', 'teacher_code', 'get_teacher_name')
    list_filter = ('is_teacher',)
    search_fields = ('username', 'first_name', 'phone_number', 'teacher_code')
    ordering = ('-is_teacher', 'username')
    
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('개인정보', {'fields': ('first_name', 'phone_number', 'is_teacher', 'teacher_code', 'teacher')}),
        ('권한', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('중요한 일정', {'fields': ('last_login', 'date_joined')}),
    )
    
    def get_teacher_name(self, obj):
        return obj.teacher.username if obj.teacher else '-'
    get_teacher_name.short_description = '담당 선생님'

class TodoAdmin(admin.ModelAdmin):
    list_display = ('user', 'content', 'is_completed', 'created_at', 'get_teacher')
    list_filter = ('is_completed', 'created_at', 'user__teacher')
    search_fields = ('content', 'user__username')
    ordering = ('-created_at',)
    
    def get_teacher(self, obj):
        return obj.user.teacher.username if obj.user.teacher else '-'
    get_teacher.short_description = '담당 선생님'

class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('user', 'date', 'get_teacher')
    list_filter = ('date', 'user__teacher')
    search_fields = ('user__username',)
    ordering = ('-date',)
    
    def get_teacher(self, obj):
        return obj.user.teacher.username if obj.user.teacher else '-'
    get_teacher.short_description = '담당 선생님'

admin.site.register(User, CustomUserAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Attendance, AttendanceAdmin)