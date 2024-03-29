# Generated by Django 4.0.5 on 2022-09-26 14:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_users', '0007_alter_staffbankaccount_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='address',
            unique_together=set(),
        ),
        migrations.AlterUniqueTogether(
            name='bankaccount',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='guardian',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='staff',
            name='phone_number',
        ),
        migrations.RemoveField(
            model_name='student',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='address',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bankaccount',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='phonenumber',
            name='account',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='address',
            unique_together={('account', 'save_name')},
        ),
        migrations.AlterUniqueTogether(
            name='bankaccount',
            unique_together={('account', 'save_name')},
        ),
        migrations.RemoveField(
            model_name='address',
            name='guardian',
        ),
        migrations.RemoveField(
            model_name='address',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='address',
            name='student',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='guardian',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='staff',
        ),
        migrations.RemoveField(
            model_name='bankaccount',
            name='student',
        ),
    ]
