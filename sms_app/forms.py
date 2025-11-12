from django import forms
from .models import Student
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentForm(forms.ModelForm):
    """
    A Django ModelForm for handling input and validation for Student instances.

    This form maps fields from the Student model and applies labels and widgets
    for rendering HTML inputs in the frontend.

    Attributes:
        Meta (class): Configures the form to use the Student model and specifies 
                      field labels and widget styling.
    """

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
    """
    A custom user registration form that extends Django's UserCreationForm.

    Adds an email field to the default registration form and specifies the fields to be displayed.
    
    Attributes:
        email (EmailField): Required field for the user's email address.

        Meta (class): Specifies the model and form fields to use for rendering and validation.
    """
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']