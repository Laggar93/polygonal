# Generated by Django 3.2.4 on 2022-01-17 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0003_alter_project_page_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project_images',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_list',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='project_page',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
