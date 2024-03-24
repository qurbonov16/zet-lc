from django.contrib import admin
from .models import *


# class TeacherAdmin(admin.ModelAdmin):
#     list_display = ('full_name', 'phone_number', 'email')
#     search_fields = ['full_name']


admin.site.register(TeacherModel)
admin.site.register(StudentModel)


class LevelAdmin(admin.ModelAdmin):
    list_display = ('level_name', 'price_level')
    search_fields = ['level_name', 'price_level']


admin.site.register(LevelModel, LevelAdmin)
admin.site.register(task_for_stuent)


class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('exercise_name', 'unit_name')
    search_fields = ['exercise_name']
