# Generated by Django 3.2.4 on 2021-10-20 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('test', models.CharField(blank=True, max_length=1000)),
                ('test_ru', models.CharField(blank=True, max_length=1000, null=True)),
                ('test_en', models.CharField(blank=True, max_length=1000, null=True)),
                ('test_fr', models.CharField(blank=True, max_length=1000, null=True)),
            ],
        ),
    ]
