from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name']


class GradeForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['Student', '1st Grade', '2nd Grade', '3rd Grade']
