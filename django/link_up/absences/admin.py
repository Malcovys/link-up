from django.contrib import admin

from absences.models import Teacher
from absences.models import Module
from absences.models import Group
from absences.models import Student
from absences.models import TeacherModule
from absences.models import Timetable
from absences.models import Absence

class StudentAdmin(admin.ModelAdmin):
    list_display = ('name', 'matricule', 'group', 'number')

admin.site.register(Teacher)
admin.site.register(Module)
admin.site.register(Group)
admin.site.register(Student, StudentAdmin)
admin.site.register(TeacherModule)
admin.site.register(Absence)
admin.site.register(Timetable)