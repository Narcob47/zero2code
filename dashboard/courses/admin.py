from django.contrib import admin
from .models import Course, Assessment, Material, Project, Class

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
