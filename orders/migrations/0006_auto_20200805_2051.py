# Generated by Django 3.0.7 on 2020-08-05 19:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '__first__'),
        ('orders', '0005_auto_20200805_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitems',
            name='order_item',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order_item_to_lists', to='menu.MenuItem'),
        ),
    ]
