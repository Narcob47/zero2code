from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Course, Assessment, Material, Project, Class, UserProfile, Notification

# Define an inline admin descriptor for UserProfile model
# which acts a bit like a singleton
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

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'address')
    search_fields = ('user__username', 'first_name', 'last_name')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('user', 'title', 'timestamp', 'is_read')
    search_fields = ('user__username', 'title')
    list_filter = ('is_read', 'timestamp')
