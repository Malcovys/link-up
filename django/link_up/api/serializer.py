from rest_framework.serializers import ModelSerializer

from absences.models import Student
from absences.models import Teacher
from absences.models import Timetable


class StudentSerialiser(ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'group_id']

class TeacherSerialiser(ModelSerializer):

    class Meta:
        model = Teacher
        fields = ['id']

class TestSerialiser(ModelSerializer):

    class Meta:
        model = Timetable
        fields = ['id', 'date', 'time_begin', 'time_ending', 'course_id']   