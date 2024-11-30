from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='course_images/', null=True, blank=True)

    def __str__(self):
        return self.title

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
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to='class_images/', null=True, blank=True)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title