from django.core.management import BaseCommand, call_command

import csv

from app_auth.models import *
from app_users.models import *
from app_management.models import *
from app_utils.models import *
from app_finance.models import *
from app_docs.models import *
from app_campus.models import *
from app_course.models import *

class Command(BaseCommand):
    
    models = (
        (Account, 'accounts.csv'),
        (Staff, 'staffs.csv'),
        (Guardian, 'guardians.csv'),
        (Student, 'students.csv'),
        (BankAccount, 'bank-accounts.csv'), # parent
        (StaffBankAccount, 'staff-bank-accounts.csv'), # child of BankAccount
        (StudentBankAccount, 'student-bank-accounts.csv'), # child of BankAccount
        (Address, 'addresses.csv'), # parent
        (StaffAddress, 'staff-addresses.csv'), # child of Address
        (StudentAddress, 'student-addresses.csv'), # child of Address
    )

    def load_data(self, model, filename):
        with open(f"./fake_data/{filename}", 'r') as f:
            reader = csv.DictReader(f, delimiter=',')
            for row in reader:
                model.objects.create(**row)
            print(f"{filename} is loaded")

    def handle(self, *args, **options):
        call_command('flush', '--verbosity=0')
        for model in self.models:
            self.load_data(model[0], model[1])
        
        print('Done')