from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    student_num = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    ap_score = models.FloatField()

    def __str__(self):
        return f"Student: {self.name} {self.surname}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
"""
Filename: Models

This function is the model of the system of how it will be formatted
"""

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):
    student_num = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    ap_score = models.FloatField()

    def __str__(self):
        return f"Student: {self.name} {self.surname}"
    
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)