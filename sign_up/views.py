from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect

from learning_center.models import StudentModel, TeacherModel
from .forms import Signup_form, LoginForm, SignTeacher
from django.contrib.auth import login, authenticate, logout

from .models import CustomUser


def registration_view(request):
    form = Signup_form()
    # print(form)
    if request.method == 'POST':
        form = Signup_form(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            usr = CustomUser.objects.all()[::-1]
            id = usr[0]
            a1 = StudentModel.objects.create(student=id)
            print(a1, "ohirgi user ")

            return redirect('login')

    return render(request, 'registration.html', context={
        'form': form
    })


def login_view(request):
    forms = LoginForm()
    if request.method == 'POST':
        forms = LoginForm(request.POST)
        if forms.is_valid():
            user = authenticate(
                username=forms.cleaned_data['username'],
                password=forms.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            forms.add_error('password', 'Parol yoki username noto\'g\'ri !')

    return render(request, 'login.html', context={
        "form": forms
    })


# def logout_view(request):
#     logout(request)
#     return redirect('login')

def logout_page(request):
    return render(request, 'logout.html')


def logout_confirm(request):
    if request.method == 'POST':
        if request.POST.get('confirm') == 'Ha':
            # Perform logout functionality here
            logout(request)
            return redirect('login')  # Redirect to home page after logout
        elif request.POST.get('confirm') == 'Yoq':
            return redirect('home')  # Redirect to home page if user chooses not to logout
    return redirect('home')  # Redirect to home page if not a POST request or invalid input


def registration_view2(request):
    form = SignTeacher()
    # print(form)
    if request.method == 'POST':
        form = SignTeacher(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            del form.cleaned_data['confirm_password']
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            print(user, user.is_teacher)
            usr = CustomUser.objects.all()[::-1]
            id = usr[0]
            a1 = TeacherModel.objects.create(teacher=id)
            print(a1, "ohirgi user ")


            return redirect('login')

    return render(request, 'regstr.html', context={
        'form': form
    })