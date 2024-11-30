from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.course_list, name='courses'),
    path('materials/', views.material_list, name='materials'),
    path('classes/', views.class_list, name='classes'),
    path('assessments/', views.assessment_list, name='assessments'),
    path('projects/', views.project_list, name='projects'),
    
    
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('assessment/<slug:slug>/', views.assessment_detail, name='assessment_detail'),
    
    path('material/<slug:slug>/', views.material_detail, name='material_detail'),
    
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    
    
    # path('challenges/', views.challenge_list, name='challenges'),
    path('notifications/', views.notifications, name='notifications'),
    path('account/', views.account, name='account'),
    path('settings/', views.settings, name='settings'),
    
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
]