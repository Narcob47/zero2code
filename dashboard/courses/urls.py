from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    #Home Page
    path('', views.login_view, name='login'),
    
    #Drawer Navigation
    path('dashboard/', views.dashboard, name='dashboard'),
    path('courses/', views.course_list, name='courses'),
    path('materials/', views.material_list, name='materials'),
    path('classes/', views.class_list, name='classes'),
    path('assessments/', views.assessment_list, name='assessments'),
    path('projects/', views.project_list, name='projects'),
    path('recordings/', views.recording_list, name='recordings'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('support/', views.support, name='support'),
    path('next/', views.next_view, name='next_view'),
    
    
    #Header Navigation
    path('profile/', views.profile, name='profile'),
    path('change-password/', views.change_password, name='change_password'),
    path('notifications/', views.notifications, name='notifications'),
    path('settings/', views.settings, name='settings'),
   
    #Individual Pages 
    path('assessments/<slug:slug>/', views.assessment_detail, name='assessment_detail'),
    path('assessments/<slug:slug>/submit/', views.submit_assessment, name='submit_assessment'),
    path('notifications/view/<int:notification_id>/', views.view_notification, name='view_notification'),
    path('notifications/delete/<int:notification_id>/', views.delete_notification, name='delete_notification'),
    path('recordings/<int:pk>/', views.recording_detail, name='recording_detail'),
    path('course/<slug:slug>/', views.course_detail, name='course_detail'),
    path('assessment/<slug:slug>/', views.assessment_detail, name='assessment_detail'),
    path('material/<slug:slug>/', views.material_detail, name='material_detail'),
    path('project/<slug:slug>/', views.project_detail, name='project_detail'),
    path('support/success/', views.support_success, name='support_success'),
    
]
