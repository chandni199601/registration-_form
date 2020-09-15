from django.db import models


# Create your models here.
class Employee(models.Model):
    eid = models.CharField(max_length=20)
    ename = models.CharField(max_length=200)
    eemail = models.CharField(max_length=100)
    econtact = models.CharField(max_length=90)
