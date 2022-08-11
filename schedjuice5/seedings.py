from django_seed import Seed
from app_users.models import *
from app_finance.models import *
from app_auth.models import *
import random
import datetime

seeder = Seed.seeder()


def addEntity():
    seeder.add_entity(
        Account,
        3,
        {
            "email": lambda x: seeder.faker.email(),
            "password": lambda x: seeder.faker.password(),
            "is_active": lambda x: True,
            "is_staff": lambda x: False,
            "is_superuser": lambda x: False,
        },
    )

    seeder.add_entity(
        Staff,
        10,
        {
            "name": lambda x: seeder.faker.name(),
            "account": lambda x: random.choice(Account.objects.all()),
        },
    )

    seeder.add_entity(
        Record,
        10,
        {
            "name": lambda x: "Record " + seeder.faker.name(),
            "bank_type": lambda x: random.choice(["KBZ", "AYA", "CB", "KBZ_Pay"]),
        },
    )

    inserted_pks = seeder.execute()
    return inserted_pks


def dyamicAddEntity(model, count, **kwargs):
    fields = [
        (field.name, field.get_internal_type())
        for field in model._meta.get_fields()
        if field.name not in ["id", "last_login"]
        and field.get_internal_type()
        not in ["ForeignKey", "ManyToManyField", "OneToOneField"]
    ]

    def get_value(name, field_type):
        if name in kwargs:
            return random.choice(kwargs[name])
        elif name == "name":
            return seeder.faker.name()
        elif name == "email":
            return seeder.faker.email()
        elif name == "password":
            return seeder.faker.password()
        elif name == "is_active":
            return True
        elif name == "is_staff":
            return False
        elif name == "is_superuser":
            return False
        elif name == "id":
            return None
        else:
            if field_type == "BooleanField":
                return random.choice([True, False])
            elif field_type == "IntegerField":
                return random.randint(1, 100)
            elif field_type == "DateTimeField":
                return f"{seeder.faker.date_time_this_year()}"
            elif field_type == "CharField":
                return "abcabc"
            else:
                raise Exception(f"{name} is not a valid field name for {model}")

    seeder.add_entity(
        model,
        count,
        {field[0]: lambda x: get_value(field[0], field[1]) for field in fields},
    )

    inserted_pks = seeder.execute()
    return inserted_pks
