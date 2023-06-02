import csv

from django.core.management import BaseCommand, CommandError, call_command

from app_auth.models import Account
from app_auth.serializers import AccountSerializer
from app_auth.views import AccountListView
from app_users.serializers import StaffSerializer, StudentSerializer
from app_users.views import StaffListView, StudentListView


class Command(BaseCommand):

    # the 'view' arg is a bit hacky. But, oh well, will refactor later
    def load_data(self, csv_file_loc: str, serializer, view):
        with open(csv_file_loc) as f:
            reader = csv.DictReader(f, delimiter=",")

            self.stdout.write(f"Loading {csv_file_loc}", ending="\n")
            accounts_data = []
            user_data = []
            for i in reader:
                accounts_data.append(
                    {"email": i["email"], "password": "123!#$sfk", "ms_id": i["ms_id"]}
                )

                transformed_data = {
                    **i,
                    "gender": i.get("gender") if i.get("gender") else "female",
                    "account": int(i["id"]),
                }
                transformed_data.pop("ms_id")
                user_data.append(transformed_data)

            accounts = AccountSerializer(
                data=accounts_data,
                context={"skip_ms_creation": True, "view": AccountListView},
                many=True,
            )
            if accounts.is_valid():
                self.stdout.write("accounts created", ending="\n")
                accounts.save()
            else:
                raise CommandError(f"Validation error. {accounts.errors}")
            email_map = {}
            for i in Account.objects.all():
                email_map[i.email] = i.id

            for i in user_data:
                i["account"] = email_map[i["email"]]
                i.pop("email")

            users = serializer(
                data=user_data,
                context={"skip_ms_creation": True, "view": view},
                many=True,
            )
            if users.is_valid():
                users.save()
                self.stdout.write(f"{i['id']}", ending="\n")
            else:
                raise CommandError(f"Validation error. {users.errors}")

    def handle(self, *args, **options):
        call_command("flush", "--verbosity=1")
        self.load_data(
            "./schedjuice5/old_data/staff.csv", StaffSerializer, StaffListView
        )
        self.stdout.write(
            self.style.SUCCESS(f"Staff data successfully imported."), ending="\n\n"
        )

        self.load_data(
            "./schedjuice5/old_data/student.csv", StudentSerializer, StudentListView
        )
        self.stdout.write(
            self.style.SUCCESS(f"Student data successfully imported."), ending="\n\n"
        )

        self.stdout.write(
            self.style.SUCCESS(f"Data importing completed."), ending="\n\n"
        )
