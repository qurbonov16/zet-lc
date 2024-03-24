from django.core.validators import FileExtensionValidator
from django.db import models
from learning_center.validators import validate_phone_number, full_name, address
from sign_up.models import *
from django.utils.translation import gettext_lazy as _


class LevelModel(models.Model):
    LEVEL_CHOICES = [
        ('A1 - Beginner', 'A1 - Beginner'),
        ('A2 - Elementary', 'A2 - Elementary'),
        ('B1 - Pre Intermediate', 'B1 - Pre Intermediate'),
        ('B1+ - Intermediate', 'B1+ - Intermediate'),
        ('B2 - Upper Intermediate', 'B2 - Advanced'),
        ('IELTS', 'IELTS')
    ]
    image = models.ImageField(upload_to='media')
    text = models.TextField(max_length=500)
    level_name = models.CharField(max_length=35, choices=LEVEL_CHOICES)
    price_level = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f'{self.level_name} + {self.price_level}'

    class Meta:
        verbose_name = 'Level'
        verbose_name_plural = 'Levels'

    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''

        return url


class TeacherModel(models.Model):
    teacher = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher.full_name}    {self.teacher.username}'


class StudentModel(models.Model):
    student = models.OneToOneField(CustomUser, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student.full_name}    {self.student.username}'


class BitirganStudent(models.Model):
    ielts_choice = [
        ('6.5', '6.5'),
        ('7', '7'),
        ('7.5', '7.5'),
        ('8', '8'),
        ('8.5', '8.5'),
        ('9', '9'),
    ]
    full_name = models.CharField(max_length=50)
    description = models.TextField()
    end_of_date = models.DateField()
    image = models.ImageField(upload_to='media')
    ielts = models.CharField(max_length=3, choices=ielts_choice)

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = 'Bitiruvchi'
        verbose_name_plural = 'Bitiruvchilar'


class task_for_stuent(models.Model):
    teacher = models.OneToOneField(TeacherModel, on_delete=models.SET_NULL, null=True, blank=True)
    student = models.ForeignKey(StudentModel, on_delete=models.CASCADE)
    level = models.ForeignKey(LevelModel, on_delete=models.CASCADE)
    video = models.FileField(upload_to='videos', validators=[
        FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    description = models.TextField(max_length=500)

    def __str__(self):
        return self.level.level_name + ' ' + self.student.student.full_name

    class Meta:
        verbose_name = 'Task'
        verbose_name_plural = 'Tasks'

# class Student(models.Model):
#     GENDER_CHOICES = [
#         ('M', 'Male'),
#         ('F', 'Female')
#     ]
#     first_name = models.CharField(max_length=20)
#     last_name = models.CharField(max_length=25, null=True, blank=True)
#     age = models.PositiveIntegerField(default=7, null=True, blank=True)
#     gender = models.CharField(max_length=1, choices=GENDER_CHOICES, null=True, blank=True)
#     image = models.ImageField(null=True, blank=True)
#     phone_number = models.CharField(max_length=13, validators=[validate_phone_number])
#     email = models.EmailField()
#     date_of_birth = models.DateField(null=True, blank=True)
#     address = models.CharField(max_length=100, validators=[validate_phone_number], null=True, blank=True)
#     teacher_id = models.ForeignKey(TeacherModel, on_delete=models.CASCADE, null=True, blank=True)
#     level_id = models.ForeignKey(LevelModel, on_delete=models.CASCADE, null=True, blank=True)
#
#     def __str__(self):
#         return f'{self.first_name} + {self.last_name} + {self.age}'
#
#     class Meta:
#         verbose_name = 'Student'
#         verbose_name_plural = 'Students'
#
#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#
#         return url


# class Exercise(models.Model):
#     exercise_name = models.CharField(max_length=50)
#     video = models.FileField(upload_to='videos', validators=[
#         FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
#     unit_name = models.CharField(max_length=20)
#     student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
#     level_id = models.ForeignKey(LevelModel, on_delete=models.CASCADE)
