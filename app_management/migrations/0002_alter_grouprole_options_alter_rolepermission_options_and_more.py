# Generated by Django 4.0.5 on 2022-08-16 13:16

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0002_alter_staffaddress_unique_together_and_more"),
        ("app_course", "0002_alter_calendar_config_alter_calendar_name_and_more"),
        ("app_management", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="grouprole",
            options={},
        ),
        migrations.AlterModelOptions(
            name="rolepermission",
            options={},
        ),
        migrations.AlterModelOptions(
            name="staffcourse",
            options={},
        ),
        migrations.AlterModelOptions(
            name="staffdepartment",
            options={},
        ),
        migrations.AlterModelOptions(
            name="staffevent",
            options={},
        ),
        migrations.AlterModelOptions(
            name="staffgroup",
            options={},
        ),
        migrations.AlterModelOptions(
            name="staffrole",
            options={},
        ),
        migrations.RenameField(
            model_name="staffevent",
            old_name="session",
            new_name="event",
        ),
        migrations.AlterField(
            model_name="department",
            name="description",
            field=models.TextField(default="..."),
        ),
        migrations.AlterField(
            model_name="department",
            name="name",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Field must only contain basic Latin characters and spaces.",
                        regex="[a-zA-Z ]",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="department",
            name="parent_id",
            field=models.ForeignKey(
                help_text="The parent department of the current department.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_management.department",
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="description",
            field=models.TextField(default="..."),
        ),
        migrations.AlterField(
            model_name="group",
            name="name",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Field must only contain basic Latin characters and spaces.",
                        regex="[a-zA-Z ]",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="group",
            name="parent_id",
            field=models.ForeignKey(
                help_text="The parent group of the current group.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_management.group",
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="credit_per_session",
            field=models.PositiveIntegerField(
                help_text="The monetary value the job generates for the assigned Staff per assigned Event."
            ),
        ),
        migrations.AlterField(
            model_name="job",
            name="description",
            field=models.TextField(default="..."),
        ),
        migrations.AlterField(
            model_name="job",
            name="name",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Field must only contain basic Latin characters and spaces.",
                        regex="[a-zA-Z ]",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="role",
            name="name",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Field must only contain basic Latin characters and spaces.",
                        regex="[a-zA-Z ]",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="is_under",
            field=models.ForeignKey(
                help_text="The Staff that the current staff is under the authority of.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="app_management.staffdepartment",
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="job",
            field=models.ForeignKey(
                help_text="The job that the Staff does in this particular relation.",
                on_delete=django.db.models.deletion.PROTECT,
                to="app_management.job",
            ),
        ),
        migrations.AlterUniqueTogether(
            name="grouprole",
            unique_together={("group", "role")},
        ),
        migrations.AlterUniqueTogether(
            name="rolepermission",
            unique_together={("role", "permission")},
        ),
        migrations.AlterUniqueTogether(
            name="staffcourse",
            unique_together={("staff", "course")},
        ),
        migrations.AlterUniqueTogether(
            name="staffdepartment",
            unique_together={("staff", "department")},
        ),
        migrations.AlterUniqueTogether(
            name="staffevent",
            unique_together={("staff", "event")},
        ),
        migrations.AlterUniqueTogether(
            name="staffgroup",
            unique_together={("staff", "group")},
        ),
        migrations.AlterUniqueTogether(
            name="staffrole",
            unique_together={("staff", "role")},
        ),
    ]
