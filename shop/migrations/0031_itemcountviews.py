# Generated by Django 3.2.4 on 2022-01-07 16:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0030_auto_20220107_1441'),
    ]

    operations = [
        migrations.CreateModel(
            name='itemcountviews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sesId', models.CharField(db_index=True, max_length=150)),
                ('itemId', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.item')),
            ],
        ),
    ]
