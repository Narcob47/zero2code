from django.db import models
from django.contrib.auth.models import User

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.title
    
class CourseModule(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='modules')
    module = models.CharField(max_length=200)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.module

class Assessment(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='assessments/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='assessments')

    def __str__(self):
        return self.title

class Material(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='materials/')
    image = models.ImageField(upload_to='material_images/', null=True, blank=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    
    

class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    file = models.FileField(upload_to='projects/')
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='projects')

    def __str__(self):
        return self.title
    
class Class(models.Model):
    title = models.CharField(max_length=200)
    date = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)
    link = models.URLField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classes')

    def __str__(self):
        return self.title

class Recording(models.Model):
    title = models.CharField(max_length=200)
    video_link = models.URLField()
    preview_image = models.URLField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='recordings')
    class_fk = models.ForeignKey(Class, on_delete=models.CASCADE, related_name='recordings')

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    address = models.TextField(blank=True)
    profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)

    def __str__(self):
        return self.user.username
    
class Notification(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=200)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    deleted = models.BooleanField(default=False)  # New field to mark notifications as deleted

    def __str__(self):
        return self.title
