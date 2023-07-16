from django.shortcuts import render
from django.shortcuts import HttpResponse

from absences.models import Student

def testview(request):
    student = Student(name='HAJANIAINA Mamitiana',
                       matricule='FI2301-168',
                       group_id=2,
                       number=28)
    student.save()
    return HttpResponse(f"""<p>{student.name} is saved</p>""")
