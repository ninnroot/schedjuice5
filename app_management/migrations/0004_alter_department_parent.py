# Generated by Django 4.1.2 on 2022-11-09 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_management", "0003_rename_parent_id_department_parent_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="department",
            name="parent",
            field=models.ForeignKey(
                help_text="The parent department of the current department.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sub_departments",
                to="app_management.department",
            ),
        ),
    ]
