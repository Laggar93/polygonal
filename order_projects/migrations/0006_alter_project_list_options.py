# Generated by Django 3.2.4 on 2022-01-17 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order_projects', '0005_auto_20220117_1753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project_list',
            options={'ordering': ['order'], 'verbose_name': 'Список проектов', 'verbose_name_plural': 'Списки проектов'},
        ),
    ]
