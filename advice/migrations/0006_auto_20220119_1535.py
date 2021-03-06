# Generated by Django 3.2.4 on 2022-01-19 12:35

import advice.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advice', '0005_auto_20220119_1456'),
    ]

    operations = [
        migrations.AddField(
            model_name='advice_blocks',
            name='image_xs',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='image_xs2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='image_xxl',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
        migrations.AddField(
            model_name='advice_blocks',
            name='image_xxl2x',
            field=models.ImageField(blank=True, null=True, upload_to=advice.models.get_file_path),
        ),
    ]
