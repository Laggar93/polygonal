# Generated by Django 3.2.4 on 2022-01-27 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0016_auto_20220127_1859'),
    ]

    operations = [
        migrations.AddField(
            model_name='project_page',
            name='last_projects',
            field=models.CharField(blank=True, max_length=255, verbose_name='Последние работы (на главной странице)'),
        ),
    ]
