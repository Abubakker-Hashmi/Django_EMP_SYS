from django.db import models

class Employee(models.Model):
    employee_number = models.IntegerField( unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    working_experience = models.IntegerField()

    def __str__(self):
        return self.name
