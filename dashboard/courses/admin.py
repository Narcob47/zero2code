from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Course, Assessment, Material, Project, Class

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Assessment)
class AssessmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'course')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'course')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'course')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'link')
    prepopulated_fields = {'slug': ('title',)}
