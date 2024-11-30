from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, Assessment, Material, Project, Class

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
    assessments = course.assessments.all()
    materials = course.materials.all()
    projects = course.projects.all()
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'assessments': assessments,
        'materials': materials,
        'projects': projects
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
def project_list(request, slug):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})

@login_required
def notifications(request):
    return render(request, 'notifications.html')

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