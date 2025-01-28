from django.db import models


class Student(models.Model):
    admission_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    unit = models.CharField(max_length=100)
    date = models.DateField()

    def __str__(self):
        return self.admission_number




