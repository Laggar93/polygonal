# Generated by Django 3.2.4 on 2022-01-24 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0016_alter_contact_social_networks_social_network_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_main',
            name='email',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Почта'),
        ),
    ]
