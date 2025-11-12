"""
Filename: Models

This function is the model of the system of how it will be formatted
"""

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Student(models.Model):

    """
    Represents a student in the system.

    Attributes:
        student_num (int): The unique student number.
        name (str): First name of the student.
        surname (str): Last name of the student.
        email_address (str): Email address of the student.
        field_of_study (str): The academic field the student is pursuing.
        ap_score (float): The student's Admission Point Score (APS).
    """

    student_num = models.PositiveIntegerField()
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    field_of_study = models.CharField(max_length=50)
    ap_score = models.FloatField()

    def __str__(self):
        return f"Student: {self.name} {self.surname}"
    
class UserProfile(models.Model):
    """
    Extends the built-in User model with a one-to-one relationship.

    Attributes:
        user (User): The associated Django User account.
    """

    user = models.OneToOneField(User, on_delete=models.CASCADE)
