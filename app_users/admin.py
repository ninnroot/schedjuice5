from django.contrib import admin

from .models import *


# Register your models here.
@admin.register(Staff)
class StaffAdminModel(admin.ModelAdmin):
    list_display = ("name", "account")
