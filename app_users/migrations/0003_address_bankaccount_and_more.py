# Generated by Django 4.0.5 on 2022-08-09 14:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("app_users", "0002_alter_staff_options_staff_about_staff_avatar_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "house_number",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                (
                    "block_number",
                    models.CharField(
                        max_length=16,
                        null=True,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                (
                    "street_name",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters, numbers and spaces.",
                                regex="[a-zA-Z0-9 ]",
                            )
                        ],
                    ),
                ),
                (
                    "township",
                    models.CharField(
                        max_length=32,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters, numbers and spaces.",
                                regex="[a-zA-Z0-9 ]",
                            )
                        ],
                    ),
                ),
                ("city", models.CharField(max_length=64)),
                ("country", models.CharField(max_length=64)),
                (
                    "postal_code",
                    models.CharField(
                        max_length=16,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must contain only number and no white spaces.",
                                regex="[0-9]",
                            )
                        ],
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="BankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "owner_name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must only contain basic Latin characters and spaces.",
                                regex="[a-zA-Z ]",
                            )
                        ],
                    ),
                ),
                (
                    "number",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Bank account number must match this: '[\\d ]{6,20}'",
                                regex="[\\d ]{6,20}",
                            )
                        ],
                    ),
                ),
                (
                    "bank_type",
                    models.CharField(
                        choices=[
                            ("KBZ", "KBZ"),
                            ("Kpay", "Kpay"),
                            ("AYA", "AYA"),
                            ("CB", "CB"),
                        ],
                        max_length=256,
                    ),
                ),
            ],
            options={
                "ordering": ["id"],
                "abstract": False,
            },
        ),
        migrations.AlterField(
            model_name="guardian",
            name="primary_phone_number",
            field=models.CharField(
                max_length=256,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guardian",
            name="secondary_phone_number",
            field=models.CharField(
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="guardian",
            name="username",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Username must match this: '[a-zA-Z0-9_]{8,32}'",
                        regex="[a-zA-Z0-9_]{8,32}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="primary_phone_number",
            field=models.CharField(
                max_length=256,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="secondary_phone_number",
            field=models.CharField(
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="staff",
            name="username",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Username must match this: '[a-zA-Z0-9_]{8,32}'",
                        regex="[a-zA-Z0-9_]{8,32}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="primary_phone_number",
            field=models.CharField(
                max_length=256,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="secondary_phone_number",
            field=models.CharField(
                max_length=256,
                null=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Phone number must match this: '(\\+)?[0-9 ]{8,20}'",
                        regex="(\\+)?[0-9 ]{8,20}",
                    )
                ],
            ),
        ),
        migrations.AlterField(
            model_name="student",
            name="username",
            field=models.CharField(
                max_length=256,
                unique=True,
                validators=[
                    django.core.validators.RegexValidator(
                        message="Username must match this: '[a-zA-Z0-9_]{8,32}'",
                        regex="[a-zA-Z0-9_]{8,32}",
                    )
                ],
            ),
        ),
        migrations.CreateModel(
            name="StudentBankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "save_name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "bank_account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.bankaccount",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.student",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "bank_account")},
            },
        ),
        migrations.CreateModel(
            name="StudentAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "save_name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                ("address_type", models.CharField(max_length=128)),
                (
                    "address",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.address",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.student",
                    ),
                ),
            ],
            options={
                "unique_together": {("student", "address")},
            },
        ),
        migrations.CreateModel(
            name="StaffBankAccount",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "save_name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                (
                    "bank_account",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.bankaccount",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.staff",
                    ),
                ),
            ],
            options={
                "unique_together": {("staff", "bank_account")},
            },
        ),
        migrations.CreateModel(
            name="StaffAddress",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "save_name",
                    models.CharField(
                        max_length=256,
                        validators=[
                            django.core.validators.RegexValidator(
                                message="Field must match this: '[a-zA-Z0-9_\\-\\(\\) ]'",
                                regex="[a-zA-Z0-9_\\-\\(\\) ]",
                            )
                        ],
                    ),
                ),
                ("is_primary", models.BooleanField(default=False)),
                ("address_type", models.CharField(max_length=128)),
                (
                    "address",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.address",
                    ),
                ),
                (
                    "staff",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app_users.staff",
                    ),
                ),
            ],
            options={
                "unique_together": {("staff", "address")},
            },
        ),
    ]
