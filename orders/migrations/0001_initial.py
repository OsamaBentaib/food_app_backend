# Generated by Django 3.0.7 on 2020-08-05 19:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('menu', '__first__'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_type', models.CharField(max_length=100)),
                ('order_time', models.CharField(max_length=50)),
                ('order_status', models.CharField(choices=[('CREATED', 'CREATED'), ('SUBMITED', 'SUBMITED'), ('CONFIRMED', 'CONFIRMED'), ('READY', 'READY'), ('DELEVERED', 'DELEVERED'), ('CANCLED', 'CANCLED'), ('FINISHED', 'FINISHED')], max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('ordered_by', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ordered_by_name', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='accounts.PersonelAccount')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('order_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.Orders')),
                ('order_item', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='menu.MenuItem')),
            ],
        ),
    ]