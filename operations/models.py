from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_name=models.CharField()
    emp_id=models.IntegerField()
    emp_dob=models.DateField()
    emp_pos=models.CharField()
    emp_address=models.CharField()