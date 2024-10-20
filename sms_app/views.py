from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
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
    return render(request, 'sms_app/index.html', {
        'students': Student.objects.all()
    })

def view_student(request, id):
    student = Student.objects.get(pk=id)
    return HttpResponseRedirect(reverse('index'))
@login_required
def add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            new_student_num =form.cleaned_data['student_num']
            new_name = form.cleaned_data['name']
            new_surname = form.cleaned_data['surname']
            new_email = form.cleaned_data['email_address']
            new_field_of_study = form.cleaned_data['field_of_study']
            new_ap_score = form.cleaned_data['ap_score']

            new_student = Student(
                student_num = new_student_num,
                name = new_name,
                surname = new_surname,
                email_address = new_email,
                field_of_study = new_field_of_study,
                ap_score = new_ap_score
            )

            new_student.save()
            return render(request, 'sms_app/add.html', {
                'form': StudentForm(),
                'success': True
            })
    else:
        form = StudentForm()
        return render(request, 'sms_app/add.html', {
            'form': StudentForm()
        })
    

def register(request):
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
    logout(request)
    return redirect('login')

@login_required
def view_student(request):
    return render(request, 'index.html')

def edit(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return render(request, 'sms_app/edit.html', {
                'form': form,
                'success': True
            })
    else:
         student = Student.objects.get(pk=id)
         form = StudentForm(instance=student)
    return render(request, 'sms_app/edit.html', {
        'form': form
    })     

def delete(request, id):
    if request.method == 'POST':
        student = Student.objects.get(pk=id)
        student.delete()
    return HttpResponseRedirect(reverse('index'))