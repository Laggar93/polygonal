# Generated by Django 3.2.4 on 2022-01-25 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0005_about_author_about_press_about_reward'),
    ]

    operations = [
        migrations.AddField(
            model_name='about_main',
            name='number',
            field=models.PositiveIntegerField(blank=True, default=1, null=True, verbose_name='Цифра'),
        ),
        migrations.AddField(
            model_name='about_main',
            name='number_text',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Подпись под цифрой'),
        ),
    ]