

from distutils.log import info
from venv import create
from rest_framework import serializers,validators
from . models import *
from dataclasses import field, fields
from django.contrib.auth.hashers import make_password


class Registerserilizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username","first_name","last_name","email","password","usertype",'Address','Gender',
                      'PhoneNumber','DateofBirth' ]

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            first_name = validated_data['first_name'],
            last_name= validated_data['last_name'],
            email = validated_data['email'],
            Address = validated_data['Address'],
            Gender = validated_data['Gender'],
            DateofBirth = validated_data['DateofBirth'],
            PhoneNumber = validated_data['PhoneNumber'],
            password = make_password(validated_data['password']),
            usertype = validated_data['usertype']
            )
    
        user.save()
        return user

class LogSerializer(serializers.Serializer):
   username = serializers.CharField(max_length=40)
   password =serializers.CharField(max_length=40)


class Userserlizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields =  ['id',"username","first_name","last_name","email","password","usertype",'Address','Gender',
                      'PhoneNumber','DateofBirth' ]






class Studentserilizer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id','user','School','studentclass','stuteacher']





class classSerilizer(serializers.ModelSerializer):
    
    class Meta:
        model = Class
        fields =['id','ClassName','school']

    # def validate_details(self,ClassName,scholl ):
    #     print("helloo -----",ClassName)

    #     if Class.objects.filter(ClassName=ClassName,scholl=scholl).exists():

    #         raise serializers.ValidationError("Not valid")
    #     else:
    #         pass

class TeacherSerilizer(serializers.ModelSerializer):
   

    class Meta:
        model = Teacher
        fields = ['id','School','user']


class Schoolserilizer(serializers.ModelSerializer):
    School_class = classSerilizer(many=True,read_only=True)
    Teacher_school  = TeacherSerilizer(many=True,read_only=True)
    School_Student  = Studentserilizer(many=True,read_only=True)



    
    class Meta:
        model = School
        fields =['id','SchoolName','City','State','School_class','Teacher_school','School_Student']


















        