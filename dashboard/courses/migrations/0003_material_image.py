# Generated by Django 5.1.3 on 2024-11-30 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='material_images/'),
        ),
    ]