from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Student
from .forms import StudentForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
@login_required
def index(request):

    """
    Display the main dashboard with a list of all students.

    :param request: The HTTP request object.
    :return: Rendered template with all student records.
    """

    return render(request, 'sms_app/index.html', {
        'students': Student.objects.all()
    })

@login_required
def add(request):
    """
    Add a new student to the system. If the request is POST and the form is valid,
    saves the student data to the database.
    """
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student = form.save()
            return render(request, 'sms_app/add.html', {
                'form': StudentForm(),
                'success': True
            })
        else:
            # Return the form with validation errors displayed
            return render(request, 'sms_app/add.html', {'form': form})
    else:
        form = StudentForm()

    return render(request, 'sms_app/add.html', {'form': form})
    

def register(request):
    """
    Register a new user. On successful registration, logs in the user.

    :param request: The HTTP request object.
    :return: Rendered registration form or redirect to index after success.
    """
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')  # Redirect to the home page or another page
    else:
        form = RegisterForm()
    return render(request, 'sms_app/register.html', {'form': form})


def login_view(request):
    """
    Authenticate and log in a user. If credentials are invalid, returns form with error messages.

    :param request: The HTTP request object.
    :return: Rendered login form or redirect to index upon success.
    """
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')  # Redirect to the home page or the student database
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request, 'sms_app/login.html', {'form': form})

def logout_view(request):
    """
    Log out the current user and redirect to the login page.

    :param request: The HTTP request object.
    :return: Redirect to login page.
    """
    logout(request)
    return redirect('login')

@login_required
def view_student(request, id ):
    """
    Display details for a specific student.

    :param request: The HTTP request object.
    :param id: Primary key of the student to display.
    :return: Rendered template with the student details.
    """
    student = get_object_or_404(Student, pk=id)
    return render(request, "sms_app/view_student.html", {"student": student})

def edit(request, id):
    """
    Edit an existing student's information.

    :param request: The HTTP request object.
    :param id: The primary key of the student to be edited.
    :return: Rendered edit form with existing or updated student data.
    """ 
    
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'sms_app/edit.html', {
                'form': form,
                'success': True
            })
    else:
         student = get_object_or_404(Student, pk=id)
         form = StudentForm(instance=student)

    return render(request, "sms_app/edit.html", {"form": form})     

def delete(request, id):
    """
    Delete a student from the database.

    :param request: The HTTP request object.
    :param id: The primary key of the student to be deleted.
    :return: Redirect to index page after deletion.
    """
    if request.method == 'POST':
        student = get_object_or_404(Student, pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))