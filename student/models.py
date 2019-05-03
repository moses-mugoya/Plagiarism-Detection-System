from .validation import validate_file_extension
from django.db import models
from django.conf import settings
from django.urls import reverse


class Student(models.Model):
    reg_number = models.CharField(max_length=13)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    document = models.FileField(upload_to='Documents/%Y/%m/%d', validators=[validate_file_extension])

    def get_absolute_url(self):
        return reverse('student:plagiarism', args=[self.id])

