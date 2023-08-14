from django.db import models

# Create your models here.
class StudentModel(models.Model):
    roll = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    father_name = models.CharField(max_length=30)
    address = models.TextField()
    
    def __str__(self):
        return f"Name: {self.name}"
    
# Model Inheritance: 1. Abstract Base Class ========================
class CommonInfoClass(models.Model): # abstract class
    name = models.CharField(max_length=20)
    city = models.CharField(max_length=50)
    class Meta: # Meta: class er sathe akta extra characteristics / behavior add kore
        abstract = True # by default onnanno class gulote eta False thake
                # abstract = True:
                # - ai class er akhn r kono object toiri kora jabe na
                # - ai class er kono typer er model toiri hobe na
                # - ai class ta diye kono type er form toiri kora jabe na
    
class StudentInfoModel(CommonInfoClass):
    roll = models.IntegerField()
    payment = models.IntegerField()
    section = models.CharField(max_length=20)
    
class TeacherInfoModel(CommonInfoClass):
    salary = models.IntegerField()
    

# Model Inheritance: 2. Multitable Inheritance =======================
class EmployeeModel(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=40)
    designation = models.CharField(max_length=30)
    
class ManagerModel(EmployeeModel):
    take_interview = models.BooleanField()
    hiring = models.BooleanField()
    
# Model Inheritance: 3. Proxy Model Inheritance =======================
class Friend(models.Model):
    school = models.CharField(max_length=40)
    section = models.CharField(max_length=10)
    attendance = models.BooleanField(max_length=10)
    hw = models.CharField(max_length=50)
    
class Me(Friend):
    class Meta:
        proxy = True
        ordering = ['id']
        
# One To One Relationship ========================================
class Person(models.Model):
    name = models.CharField(max_length=30)
    city = models.CharField(max_length=50)
    email = models.EmailField(max_length=30)
    
    def __str__(self):
        return self.name
    
class Passport(models.Model):
    user = models.OneToOneField(to = Person, on_delete=models.CASCADE)
    pass_number = models.IntegerField()
    page = models.IntegerField()
    validity = models.IntegerField()
    
# Many To One Relationship ========================================
class Post(models.Model):
    user = models.ForeignKey(Person, on_delete=models.SET_NULL, null=True)
    post_cap = models.CharField(max_length=30)
    post_details = models.CharField(max_length=100)
    
# Many To Many Relationship ========================================
class Student(models.Model):
    name = models.CharField(max_length=30)
    roll = models.IntegerField()
    class_name = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name
    
class Teacher(models.Model):
    student = models.ManyToManyField(Student, related_name='teachers') # many to many relationship e cascade kaj kore na
    name = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    mobile = models.CharField(max_length=11)
    
    def student_list(self):
        return ", ".join([str(i) for i in self.student.all()])