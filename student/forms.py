from django import forms
from .models import Student
from django.core.validators import RegexValidator


class StudentForm(forms.ModelForm):
    my_validator = RegexValidator("\w{5}\-\d{4}\-\d{2}", "Reg_number format needs to be #####-####-##.")
    reg_number = forms.CharField(min_length=13, max_length=13, validators=[my_validator])
    
    class Meta:
        model = Student
        fields = ('reg_number', 'document')

