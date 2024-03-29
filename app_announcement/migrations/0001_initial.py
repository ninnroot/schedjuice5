# Generated by Django 4.0.5 on 2022-09-23 05:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app_users', '0006_alter_studentaddress_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=256, validators=[django.core.validators.RegexValidator(message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'", regex='[a-zA-Z0-9_\\-\\(\\) ]')])),
                ('body', models.TextField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_users.staff')),
            ],
            options={
                'ordering': ['id'],
                'abstract': False,
            },
        ),
    ]
