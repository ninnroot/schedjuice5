import csv

from django.core.management import BaseCommand, call_command

from app_auth.models import *
from app_campus.models import *
from app_course.models import *
from app_docs.models import *
from app_finance.models import *
from app_management.models import *
from app_users.models import *
from app_utils.models import *
from app_announcement.models import *
from app_assignment.models import *


class Command(BaseCommand):

    models = (
        # app_users
        (Account, "accounts.csv"),
        (PhoneNumber, "phone_numbers.csv"),
        (Staff, "staffs.csv"),
        (Guardian, "guardians.csv"),
        (Student, "students.csv"),
        (BankAccount, "bank-accounts.csv"),  # parent
        (Address, "addresses.csv"),  # parent
        # app_campus
        (VenueClassification, "venue-classification.csv"),
        (Campus, "campus.csv"),
        (Venue, "venue.csv"),
        # app_course
        (Category, "category.csv"),
        (EventClassification, "event-classification.csv"),
        (Course, "course.csv"),
        (Event, "event.csv"),
        (EventVenue, "event-venue.csv"),
        (Calendar, "calendar.csv"),
        # app_finance
        (Record, "record.csv"),
        # app_management
        (Group, "group.csv"),
        (Department, "department.csv"),
        (Job, "job.csv"),
        (Role, "role.csv"),
        (Permission, "permission.csv"),
        (StaffGroup, "staff-group.csv"),
        (StaffDepartment, "staff-department.csv"),
        (StaffCourse, "staff-course.csv"),
        (StaffEvent, "staff-event.csv"),
        (StaffRole, "staff-role.csv"),
        (GroupRole, "group-role.csv"),
        (StudentCourse, "students-courses.csv"),
        (RolePermission, "role-permission.csv"),
        # app_announcement
        (Announcement, "announcements.csv"),
        # app_assignment
        (Assignment, "assignments.csv"),
        (Attachment, "assignment-attachments.csv"),
        (Submission, "submission.csv"),
        (SubmissionAttachment, "submission-attachments.csv"),
    )

    def load_data(self, model, filename):
        with open(f"./fake_data/{filename}", "r") as f:
            reader = csv.DictReader(f, delimiter=",")
            for row in reader:
                model.objects.create(**row)
            print(f"{filename} is loaded")

    def handle(self, *args, **options):
        call_command("flush", "--verbosity=0")
        for model in self.models:
            self.load_data(model[0], model[1])

        print("Done")
