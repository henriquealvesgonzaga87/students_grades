from django.db import models


class Student(models.Model):
    name = models.CharField('name', max_length=200)
    register = models.IntegerField('register number')

    def __str__(self):
        return f'name: {self.name}, register number: {self.register}'
