from django.shortcuts import render
from django.shortcuts import HttpResponse

from absences.models import Student

def testview(request):
    return HttpResponse(f"""<p>Un, deux test</p>""")
