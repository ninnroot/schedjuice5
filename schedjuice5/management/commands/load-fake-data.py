from django.core.management.base import BaseCommand, CommandError
from django.core.management import call_command
from schedjuice5.seedings import addEntity, dyamicAddEntity
from app_users.models import *
from app_finance.models import *
from app_auth.models import *


class Command(BaseCommand):
    help = "Help to seed the database"

    def handle(self, *args, **options):
        call_command("flush")
        call_command("seed", "app_auth", "--number=10", verbosity=0)
        call_command("seed", "app_docs", "--number=10", verbosity=0)
        call_command("seed", "app_finance", "--number=10", verbosity=0)
        call_command("seed", "app_users", "--number=10", verbosity=0)
