# Generated by Django 3.0.7 on 2020-08-13 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20200812_1647'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurantaccount',
            name='points',
            field=models.IntegerField(default=0),
        ),
    ]