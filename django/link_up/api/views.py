from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

from api.serializer import StudentSerialiser
from absences.models import Student

import json

class StudentView(APIView):

    serializer_class = StudentSerialiser

    def getStudent(self, user_id):
        student = Student.objects.get(user_id=user_id)
        return {'name':student.name, 'group_id':student.group_id}

    def auth(self, username, password):
        try:
            user = User.objects.get(username=username)
            if user.check_password(password):
                return {'user':user, 'state':1}
            else:
                return {'message':'password_incorect', 'state':0}
        except User.DoesNotExist:
            return {'message':'user_name_incorect', 'state':0}

    def get(self, request, *args, **kwargs):
        json_data = json.loads(request.body)
        username = json_data.get('name')
        password = json_data.get('password')

        auth_result = self.auth(username=username, password=password)

        if not auth_result['state']:
            return Response({'message': auth_result['message']}, status=status.HTTP_401_UNAUTHORIZED)

        user = auth_result.get('user')
        student = self.getStudent(user.id)

        serialiser = StudentSerialiser(student)
        return Response(serialiser.data)

