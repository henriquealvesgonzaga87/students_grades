from django.db import models


class Student(models.Model):
    id = models.SmallAutoField('id', primary_key=True)
    name = models.CharField('name', max_length=500)

    def __str__(self):
        return f"name: {self.name}"


class Grades(models.Model):
    id = models.SmallAutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    g1 = models.PositiveSmallIntegerField('1st Grade')
    g2 = models.PositiveSmallIntegerField('2nd Grade')
    g3 = models.PositiveSmallIntegerField('3rd Grade')

    def __str__(self):
        return f"student: {self.student}, 1st Grade: {self.g1}, 2nd Grade: {self.g2}, 3rd Grade: {self.g3}"
