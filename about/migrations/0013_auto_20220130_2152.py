# Generated by Django 3.2.4 on 2022-01-30 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0012_auto_20220127_2245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about_author',
            name='index_photo_lg',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='index_photo_lg2x',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='index_photo_xs',
        ),
        migrations.RemoveField(
            model_name='about_author',
            name='index_photo_xs2x',
        ),
    ]