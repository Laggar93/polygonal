# Generated by Django 3.2.4 on 2022-01-24 10:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0006_auto_20220124_1250'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_social_networks',
            options={'ordering': ['order'], 'verbose_name': 'Соц. сети в контактах', 'verbose_name_plural': 'Соц. сети в контактах'},
        ),
    ]