# Generated by Django 4.1.2 on 2022-11-03 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_course", "0005_alter_course_color"),
    ]

    operations = [
        migrations.AddField(
            model_name="event",
            name="name",
            field=models.CharField(
                blank=True,
                max_length=100,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                        regex="[a-zA-Z0-9_\\-\\(\\) ]",
                    )
                ],
            ),
        ),
    ]
