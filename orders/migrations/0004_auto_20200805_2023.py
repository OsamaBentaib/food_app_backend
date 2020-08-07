# Generated by Django 3.0.7 on 2020-08-05 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200805_2022'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='order_type',
            field=models.CharField(choices=[('DELIVERY', 'DELIVERY'), ('TAKEAWAY', 'TAKEAWAY'), ('DININ', 'DININ')], max_length=100),
        ),
    ]
