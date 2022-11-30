from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

gender = (
    ('MALE','MALE'),
    ('FEMALE', 'FEMALE')
)

usertype = (
    ('Administrator','Administrator'),
    ('AssistantTeacher','Assistant Teacher'),
    ('Regular Teacher','Regular Teacher'),
    ('Student','Student')

)

class School(models.Model):
    SchoolName = models.CharField(max_length=240)
    City       =models.CharField(max_length=240)
    State      =models.CharField(max_length=240)

    def __str__(self):
        return self.SchoolName



class Class(models.Model):
    ClassName= models.CharField(max_length=240)
    school = models.ForeignKey(School, related_name='School_class',on_delete=models.CASCADE,null=True,blank=True )
    class Meta:
        unique_together = (("ClassName", "school"),)


class User(AbstractUser):
    Address      = models.CharField(max_length=240)
    Gender         =  models.CharField(max_length=10 , choices= gender)
    PhoneNumber = models.IntegerField(null=True,blank=True)
    DateofBirth = models.DateField(null=True, blank=True)
    usertype = models.CharField(max_length=100 , choices= usertype)
    

class Teacher(models.Model):
    School = models.ForeignKey(School, related_name='Teacher_school',on_delete=models.CASCADE ,null=True,blank=True)
    user = models.OneToOneField(User, related_name='User_Teacher',on_delete=models.CASCADE ,null=True,blank=True)
    class Meta:
        unique_together = (("School", "user")) 



class  Student(models.Model):
    user = models.OneToOneField(User, related_name='User_school',on_delete=models.CASCADE ,null=True,blank=True)
    School = models.ForeignKey(School, related_name='School_Student',on_delete=models.CASCADE ,null=True,blank=True)
    studentclass = models.ForeignKey(Class, related_name='Student_class',on_delete=models.CASCADE,null=True,blank=True)
    stuteacher = models.ForeignKey(Teacher, related_name='Student_Teacher',on_delete=models.CASCADE,null=True,blank=True)

    class Meta:
        unique_together = (("studentclass", "user","School",'stuteacher'),) 




