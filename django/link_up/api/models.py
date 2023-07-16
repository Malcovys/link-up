from django.db import models


from absences.models import Timetable
from absences.models import Student


class StudentPresence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Timetable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student}'