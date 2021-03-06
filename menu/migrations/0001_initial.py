# Generated by Django 3.0.7 on 2020-08-07 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=500)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('dprice', models.DecimalField(decimal_places=2, max_digits=5)),
                ('categories', models.CharField(max_length=500)),
                ('poster', models.ImageField(max_length=90000, upload_to='menu')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('added_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('rst_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.RestaurantAccount')),
            ],
        ),
        migrations.CreateModel(
            name='Ingredients',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('poster', models.ImageField(max_length=90000, upload_to='menu/ingredients')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='makers', to='menu.MenuItem')),
            ],
            options={
                'ordering': ['id'],
                'unique_together': {('Item', 'id')},
            },
        ),
    ]
