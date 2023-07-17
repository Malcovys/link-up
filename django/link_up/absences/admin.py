from django.contrib import admin

from absences.models import Teacher
from absences.models import Module
from absences.models import Group
from absences.models import Student
from absences.models import TeacherModule
from absences.models import Timetable
from absences.models import Absence

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matricule', 'group', 'number', 'user')

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')

class TeacherModuleAdmin(admin.ModelAdmin):
    list_display = ('module', 'teacher', 'group')

class TimetableAdmin(admin.ModelAdmin):
    list_display = ('course','id', 'date', 'time_begin', 'time_ending')

class AbsenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_id', 'getDate')

    def getDate(self, Timetable):
        return Timetable.course.date

class ModuleAdmin(admin.ModelAdmin):
    list_display = ('code', 'name')

admin.site.register(Teacher, TeacherAdmin)
admin.site.register(Module, ModuleAdmin)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(TeacherModule, TeacherModuleAdmin)
admin.site.register(Absence, AbsenceAdmin)
admin.site.register(Timetable, TimetableAdmin)