from django.contrib import admin

from api.models import StudentPresence

class StudentPresenceAdmin(admin.ModelAdmin):
    list_display = ('student', 'course_id', 'getDate')

    def getDate(self, Timetable):
        return Timetable.course.date
    
admin.site.register(StudentPresence)
