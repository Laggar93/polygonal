# Generated by Django 3.2.4 on 2022-01-24 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0010_auto_20220124_1406'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact_main',
            name='address_en',
        ),
        migrations.RemoveField(
            model_name='contact_main',
            name='address_fr',
        ),
        migrations.RemoveField(
            model_name='contact_main',
            name='address_ru',
        ),
        migrations.RemoveField(
            model_name='contact_main',
            name='work_mode_en',
        ),
        migrations.RemoveField(
            model_name='contact_main',
            name='work_mode_fr',
        ),
        migrations.RemoveField(
            model_name='contact_main',
            name='work_mode_ru',
        ),
        migrations.RemoveField(
            model_name='contact_social_networks',
            name='title_en',
        ),
        migrations.RemoveField(
            model_name='contact_social_networks',
            name='title_fr',
        ),
        migrations.RemoveField(
            model_name='contact_social_networks',
            name='title_ru',
        ),
    ]