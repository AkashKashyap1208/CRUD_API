# Generated by Django 4.2 on 2023-04-05 12:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('helpers', '0001_initial'),
        ('crud_api', '0002_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='designation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_dropdown_desig', to='helpers.dropdown'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='employee_customUser', to=settings.AUTH_USER_MODEL),
        ),
    ]
