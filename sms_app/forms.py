"""
Function: Forms

This function is to register students to the system

"""

from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [ 'student_num', 'name', 'surname', 'email_address', 'field_of_study', 'ap_score']
        labels = {
             'student_num': 'Student Number',
             'name': 'Name',
             'surname': 'Surname', 
             'email_address': 'Email',
             'field_of_study': 'Field of Study', 
             'ap_score': 'AP Score'
        }
        widgets ={
            'student_num': forms.NumberInput(attrs={'class': 'form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'surname': forms.TextInput(attrs={'class': 'form-control'}),
            'email_address': forms.EmailInput(attrs={'class': 'form-control'}),
            'field_of_study': forms.TextInput(attrs={'class': 'form-control'}),
            'ap_score': forms.NumberInput(attrs={'class': 'form-control'})
        }


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']