from django.db import models
from django.db.models import Avg


class Student(models.Model):
    id = models.SmallAutoField('id', primary_key=True)
    name = models.CharField('name', max_length=500)

    def __str__(self):
        return f"id: {self.id}, name: {self.name}"


class FirstQuarter(models.Model):
    id = models.SmallAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    g_math = models.FloatField('Math')
    g_natural_sciences = models.FloatField('Natural Science')
    g_human_sciences = models.FloatField('Human Science')

    def __str__(self):
        return f"student: {self.student}, Math: {self.g_math}, Natural Science: {self.g_natural_sciences}, " \
               f"Human Science: {self.g_human_sciences}"


class SecondQuarter(models.Model):
    id = models.SmallAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    g_math = models.FloatField("Math")
    g_natural_sciences = models.FloatField("Natural Science")
    g_human_sciences = models.FloatField("Human Sciences")

    def __str__(self):
        return f"student: {self.student}, Math: {self.g_math}, Natural Science: {self.g_natural_sciences}, " \
               f"Human Science: {self.g_human_sciences}"


class ThirdQuarter(models.Model):
    id = models.SmallAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    g_math = models.FloatField("Math")
    g_natural_sciences = models.FloatField("Natural Sciences")
    g_human_sciences = models.FloatField("Human Sciences")

    def __str__(self):
        return f"student: {self.student}, Math: {self.g_math}, Natural Science: {self.g_natural_sciences}, " \
               f"Human Science: {self.g_human_sciences}"


class AverageGrades(models.Model):
    id = models.SmallAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    a_math = models.FloatField('Average Math', Avg(FirstQuarter.g_math, SecondQuarter.g_math, ThirdQuarter.g_math))
    a_natural_sciences = models.FloatField('Average Natural Sciences', Avg(FirstQuarter.g_natural_sciences,
                                                                           SecondQuarter.g_natural_sciences,
                                                                           ThirdQuarter.g_natural_sciences))
    a_human_sciences = models.FloatField('Average Human Sciences', Avg(FirstQuarter.g_human_sciences,
                                                                       SecondQuarter.g_human_sciences,
                                                                       ThirdQuarter.g_human_sciences))

    def __str__(self):
        return f"Student: {self.student}, Average Math: {self.a_math}, Average Natual Science: {self.a_natural_sciences}" \
               f"Average Human Sciences {self.a_human_sciences}"
