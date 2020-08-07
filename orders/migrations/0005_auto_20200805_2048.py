# Generated by Django 3.0.7 on 2020-08-05 19:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200805_2023'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitems',
            name='order_id',
        ),
        migrations.AddField(
            model_name='orderitems',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Order_item_lists', to='orders.Orders'),
        ),
    ]
