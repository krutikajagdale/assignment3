from django.db import models
class Student(models.Model):
    Username = models.CharField(max_length = 20)
    Password = models.CharField(max_length = 20)
    Phone_number = models.CharField(max_length = 10)
    Address = models.CharField(max_length = 100)
