from django import forms
from .models import *


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['id', 'name']


class GradeForm(forms.ModelForm):
    class Meta:
        model = FirstQuarter
        fields = ['Student', 'Math', 'Natural Science', 'Human Science']


class GradeForm2(forms.ModelForm):
    class Meta:
        model = SecondQuarter
        fields = ['Student', 'Math', 'Natural Science', 'Human Science']


class GradeForm3(forms.ModelForm):
    class Meta:
        model = ThirdQuarter
        fields = ['Student', 'Math', 'Natural Science', 'Human Science']


class AverageForm(forms.ModelForm):
    class Meta:
        model = AverageGrades
        fields = ['Student', 'Math', 'Natural Science', 'Human Science']
