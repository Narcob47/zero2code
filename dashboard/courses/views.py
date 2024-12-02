from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from .models import Course, Assessment, Material, Project, Class, UserProfile, Notification
from .forms import CustomLoginForm, UserProfileForm, UserForm

def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)
            return redirect('dashboard')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def course_list(request):
    courses = Course.objects.all()
    return render(request, 'course_list.html', {'courses': courses})

@login_required
def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug)
    modules = course.modules.all()
    return render(request, 'course_detail.html', {
        'course': course,
        'modules': modules,
    })

@login_required
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'class_list.html', {'classes': classes})

@login_required
def assessment_list(request):
    assessments = Assessment.objects.all()
    return render(request, 'assessment_list.html', {'assessments': assessments})

@login_required
def material_list(request):
    materials = Material.objects.all()
    return render(request, 'materials_list.html', {'materials': materials})

@login_required
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def notifications(request):
    all_notifications = Notification.objects.filter(deleted=False).order_by('-timestamp')
    return render(request, 'notifications.html', {'notifications': all_notifications})

@login_required
def account(request):
    return render(request, 'account.html')

@login_required
def settings(request):
    return render(request, 'settings.html')

def assessment_detail(request, slug):
    assessment = get_object_or_404(Assessment, slug=slug)
    return render(request, 'assessments/assessment_detail.html', {'assessment': assessment})

def material_detail(request):
    material = Material.objects.all()
    return render(request, 'materials_detail.html', {'material': material})

def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, 'projects/project_detail.html', {'project': project})

@login_required
def profile(request):
    user = request.user
    user_profile, created = UserProfile.objects.get_or_create(user=user)

    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=user)
        profile_form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('dashboard')
    else:
        user_form = UserForm(instance=user)
        profile_form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            return redirect('dashboard')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})

@login_required
def view_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    return render(request, 'view_notification.html', {'notification': notification})

@login_required
def delete_notification(request, notification_id):
    notification = get_object_or_404(Notification, id=notification_id)
    if request.method == 'POST':
        notification.deleted = True
        notification.save()
        return redirect('notifications')
    return render(request, 'delete_notification.html', {'notification': notification})