# Generated by Django 3.2.4 on 2022-01-21 11:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('delivery', '0003_auto_20220121_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery_columns',
            name='delivery_article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='article_columns', to='delivery.delivery_article', verbose_name='Списки статей доставки и оплаты'),
        ),
    ]
