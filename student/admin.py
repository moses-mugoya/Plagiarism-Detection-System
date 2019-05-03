from django.contrib import admin
from .models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display = ['reg_number', 'user']


admin.site.register(Student, StudentAdmin)
