# Generated by Django 4.1.2 on 2022-12-13 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0010_alter_address_account_alter_bankaccount_account_and_more"),
        (
            "app_course",
            "0008_alter_course_category_alter_event_classification_and_more",
        ),
        ("app_management", "0005_studentcourse"),
    ]

    operations = [
        migrations.AlterField(
            model_name="group",
            name="parent",
            field=models.ForeignKey(
                help_text="The parent group of the current group.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sub_groups",
                to="app_management.group",
            ),
        ),
        migrations.AlterField(
            model_name="grouprole",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups_roles",
                to="app_management.group",
            ),
        ),
        migrations.AlterField(
            model_name="grouprole",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="groups_roles",
                to="app_management.role",
            ),
        ),
        migrations.AlterField(
            model_name="rolepermission",
            name="permission",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles_permissions",
                to="app_management.permission",
            ),
        ),
        migrations.AlterField(
            model_name="rolepermission",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="roles_permissions",
                to="app_management.role",
            ),
        ),
        migrations.AlterField(
            model_name="staffcourse",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_courses",
                to="app_course.course",
            ),
        ),
        migrations.AlterField(
            model_name="staffcourse",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="staffs_courses",
                to="app_management.job",
            ),
        ),
        migrations.AlterField(
            model_name="staffcourse",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_courses",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="department",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_depts",
                to="app_management.department",
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="is_under",
            field=models.ForeignKey(
                help_text="The Staff that the current staff is under the authority of.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="sub_staffs_depts",
                to="app_management.staffdepartment",
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="job",
            field=models.ForeignKey(
                help_text="The job that the Staff does in this particular relation.",
                on_delete=django.db.models.deletion.PROTECT,
                related_name="staffs_depts",
                to="app_management.job",
            ),
        ),
        migrations.AlterField(
            model_name="staffdepartment",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_depts",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="staffevent",
            name="event",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_events",
                to="app_course.event",
            ),
        ),
        migrations.AlterField(
            model_name="staffevent",
            name="job",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name="staffs_events",
                to="app_management.job",
            ),
        ),
        migrations.AlterField(
            model_name="staffevent",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_events",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="staffgroup",
            name="group",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_groups",
                to="app_management.group",
            ),
        ),
        migrations.AlterField(
            model_name="staffgroup",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_groups",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="staffrole",
            name="role",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_roles",
                to="app_management.role",
            ),
        ),
        migrations.AlterField(
            model_name="staffrole",
            name="staff",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="staffs_roles",
                to="app_users.staff",
            ),
        ),
        migrations.AlterField(
            model_name="studentcourse",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students_courses",
                to="app_course.course",
            ),
        ),
        migrations.AlterField(
            model_name="studentcourse",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="students_courses",
                to="app_users.student",
            ),
        ),
    ]
