# Generated by Django 3.2.4 on 2022-01-27 12:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_auto_20220127_1509'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='index_main',
            options={'verbose_name': 'Главная страница', 'verbose_name_plural': 'Главная страница'},
        ),
        migrations.CreateModel(
            name='order_point',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(verbose_name='Порядок показа')),
                ('point', models.TextField(blank=True, null=True, verbose_name='Пункты списка проекта на заказ')),
                ('index', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='points', to='index.index_main', verbose_name='Пункты списка')),
            ],
            options={
                'verbose_name': 'Пункты списка',
                'verbose_name_plural': 'Пункты списка',
            },
        ),
    ]
