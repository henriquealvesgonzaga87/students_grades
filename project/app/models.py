from django.db import models


class Student(models.Model):
    id = models.BigAutoField('id', primary_key=True)
    name = models.CharField('name', max_length=200)

    def __str__(self):
        return f"name: {self.name}, id: {self.id}"
