from django.db import models

class Teacher(models.Model):
    name = models.CharField(max_length=100, null=False)
    matricule = models.CharField(max_length=200, null=False)
    active = models.fields.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

class Module(models.Model): 
    name = models.CharField(max_length=100, null=False)
    code = models.CharField(max_length=200, null=False)

    def __str__(self):
        return f'{self.name}'

class Group(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.name}'

class Student(models.Model):
    name = models.CharField(max_length=100)
    matricule = models.CharField(max_length=200)
    group = models.ForeignKey(Group, null=False, on_delete=models.CASCADE)
    number = models.IntegerField(null=False)
    active = models.fields.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

class TeacherModule(models.Model):
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE)
    module = models.ForeignKey(Module, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.teacher}'
    
class Timetable(models.Model):
    course = models.ForeignKey(TeacherModule, on_delete=models.CASCADE)
    date = models.DateField(null=False)
    time_begin = models.TimeField(null=False)
    time_ending = models.TimeField(null=False)

    def __str__(self):
        return f'{self.course}'

class Absence(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Timetable, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.student}'