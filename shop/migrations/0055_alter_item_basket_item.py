# Generated by Django 3.2.4 on 2022-03-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0054_remove_coupon_subcategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item_basket',
            name='item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.item', verbose_name='Товар'),
        ),
    ]
