# Generated by Django 3.2.4 on 2022-01-17 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0006_alter_project_list_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_images',
            name='main_photo_2',
        ),
        migrations.RemoveField(
            model_name='project_images',
            name='main_photo_3',
        ),
        migrations.RemoveField(
            model_name='project_images',
            name='main_photo_4',
        ),
    ]
