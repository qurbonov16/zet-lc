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
        widgets = {
            'level': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Level Tanlang'}),
            'video': forms.FileInput(attrs={'class': 'form', 'placeholder': 'Video Tanglang'}),
            'description': forms.Textarea(
                attrs={'class': 'form-control', 'placeholder': "Student nima qilishi kerakligini ayting"})
        }


