# Generated by Django 3.2.4 on 2022-02-09 12:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0024_project_list_first_display'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project_list',
            name='first_display',
        ),
    ]
