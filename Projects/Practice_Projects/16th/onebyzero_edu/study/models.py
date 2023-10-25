from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100)
    # location = models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} ({self.university})'

class Course(models.Model):
    title = models.CharField(max_length=100)
    code = models.CharField(max_length=10)
    credit = models.DecimalField(max_digits=4, decimal_places=1)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    
    def __str__(self):
        return self.title
    
class Question(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    year = models.PositiveIntegerField()
    semester = models.PositiveIntegerField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    exam_name = models.CharField(max_length=50)
    session = models.CharField(max_length=9)
    question_file = models.FileField(upload_to='study/questions/')

    def __str__(self):
        return self.exam_name

