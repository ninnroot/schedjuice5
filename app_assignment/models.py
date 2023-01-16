from django.db import models
from app_users.models import Staff, Student
from app_course.models import Course
from schedjuice5.models import BaseModel
from schedjuice5.validators import *

class Assignment(BaseModel):
    name = models.CharField(max_length=256, validators=[englishAndSomeSpecialValidation])
    instruction = models.TextField()
    start_date = models.DateTimeField()
    due_date = models.DateTimeField()
    grading_criteria = models.JSONField()
    is_published = models.BooleanField(default=False)
    is_first_published = models.BooleanField(default=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
        

class Attachment(BaseModel):
    attached_file = models.FileField(upload_to="assignments/questions")
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)
    

class Submission(BaseModel):
    description = models.TextField()
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE)


class SubmissionAttachment(BaseModel):
    attached_file = models.FileField(upload_to="assignments/answers")
    submission = models.ForeignKey(Submission, on_delete=models.CASCADE)



