from django.shortcuts import render, redirect
from .models import *
from .forms import TaskForm


def home_view(request):
    # teachers = TeacherModel.objects.all()/
    bts = BitirganStudent.objects.all()
    courses = LevelModel.objects.all()
    return render(request, 'home.html', {
        'courses': courses,
        'bts': bts,}
                     )


def about_view(request):
    return render(request, 'about.html')


def contact_view(request):
    return render(request, 'contact.html')


def blog_view(request):
    works = LevelModel.objects.all()
    return render(request, 'blog.html', {'works': works})


def course_dt_view(request, id):
    courses = LevelModel.objects.filter(id=id).all()

    return render(request, 'course-detail.html', {'courses': courses})


def give_task(request):
    if request.user.is_superuser == True or request.user.is_teacher == True:
        forms = TaskForm()
        print(forms)
        if request.method == 'POST':
            forms = TaskForm(request.POST, request.FILES)
            if forms.is_valid():
                forms.save()
                return redirect('home')

        return render(request, 'give_task.html',
                  {'forms': forms})
    else:
        st = request.user.id
        print(st, 'salommmmmmmm')


        try:
            tasks = task_for_stuent.objects.filter(student__student_id=st).all()
        except:
            tasks = task_for_stuent.objects.filter(student__student_id=st).all()
        print(tasks)

        return render(request, 'give_task.html', {'tasks': tasks})


