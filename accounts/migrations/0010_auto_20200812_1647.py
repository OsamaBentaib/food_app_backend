# Generated by Django 3.0.7 on 2020-08-12 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200811_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personelaccount',
            name='phone',
        ),
        migrations.CreateModel(
            name='PersonPhone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=200)),
                ('isActivate', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('added_by', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Person_phone', to='accounts.PersonelAccount')),
            ],
        ),
    ]
