# Generated by Django 5.1.3 on 2024-12-01 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_notification_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='date',
            field=models.CharField(default=879430749056847369034, max_length=200),
            preserve_default=False,
        ),
    ]
