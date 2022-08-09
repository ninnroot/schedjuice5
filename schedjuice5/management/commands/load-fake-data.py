from django.core.management.base import BaseCommand, CommandError
from schedjuice5.seedings import addEntity, dyamicAddEntity
from app_users.models import *
from app_finance.models import *
from app_auth.models import *

class Command(BaseCommand):
    help = "Help to seed the database"

    def handle(self, *args, **options):
        # dyamicAddEntity(Account, 3)
        dyamicAddEntity(Staff, 10, account=Account.objects.all())
        dyamicAddEntity(Record, 3, bank_type=["KBZ", "AYA", "CB", "KBZ_Pay"])
