from django.db import models

# Create your models here.

class Employee(models.Model):
    Id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=50)
    age=models.IntegerField(max_length=2)
    mobile=models.CharField(max_length=10,unique=True)
    email=models.EmailField(max_length=50,unique=True)
    password=models.CharField(max_length=8)
    city=models.CharField(max_length=50)
    salary=models.FloatField()

class Meta:
    db_table="empdata"

