from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Course, Assessment, Material, Project, Class, UserProfile, Notification, CourseModule, Recording

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton

class CourseModuleInline(admin.TabularInline):
    model = CourseModule
    extra = 1

class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'profile'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline,)
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
    inlines = [CourseModuleInline]
    

@admin.register(CourseModule)
class CourseModuleAdmin(admin.ModelAdmin):
    list_display = ('module', 'course', 'order')
    list_filter = ('course',)
    search_fields = ('module', 'course__title')

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
    list_display = ('title', 'slug', 'link', 'date', 'course')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'address')
    search_fields = ('user__username', 'first_name', 'last_name')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'is_read')
    search_fields = ('user__username', 'title')
    list_filter = ('is_read', 'timestamp')

@admin.register(Recording)
class RecordingAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'class_fk', 'video_link')
    list_filter = ('course', 'class_fk')
    search_fields = ('title', 'course__title', 'class_fk__title')
