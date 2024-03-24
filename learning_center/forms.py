from django import forms
from .models import task_for_stuent, StudentModel
from django.core.exceptions import ValidationError
from .models import *
task = task_for_stuent


class TaskForm(forms.ModelForm):

    student = StudentModel()

    class Meta:
        model = task_for_stuent
        fields = ['student', 'level', 'video', 'description']


    # def validate_student(self):
    #     try:
    #         x = StudentModel.objects.get(id=self.cleaned_data['student'])
    #     except:
    #         raise ValidationError('Xatolik, bunaqa ID boyica student yoq !')


