# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Student, Programme, Room, Exam


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created',
        'first_name',
        'last_name',
        'other_names',
        'student_id',
        'index_number',
        'fingerprint',
        'level',
        'programme_of_study',
    )
    list_filter = ('created', 'fingerprint', 'programme_of_study')
    raw_id_fields = ('registered_exams',)


@admin.register(Programme)
class ProgrammeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'college')
    search_fields = ('name',)


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'capacity')
    raw_id_fields = ('students', 'invigilators')
    search_fields = ('name',)


@admin.register(Exam)
class ExamAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'course_name',
        'course_code',
        'level',
        'start',
        'end',
    )
    list_filter = ('start', 'end')
    raw_id_fields = ('rooms',)
