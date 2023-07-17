from rest_framework.serializers import ModelSerializer

from absences.models import Student


class StudentSerialiser(ModelSerializer):

    class Meta:
        model = Student
        fields = ['id', 'name', 'group_id']