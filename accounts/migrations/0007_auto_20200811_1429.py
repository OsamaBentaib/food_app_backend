# Generated by Django 3.0.7 on 2020-08-11 13:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('accounts', '0006_auto_20200811_0107'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantaccount',
            name='status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='rating',
            name='rated_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='reviews',
            name='reviewed_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
